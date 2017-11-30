#encoding=utf-8
from pyspark.sql import SparkSession
from pyspark import SparkConf, SQLContext
import pandas as pd
import datetime
import re
import jieba
import numpy as np
import jieba.analyse as ja


class UserSummary(object):
    def __init__(self):
        # local test
        # self.spark = SparkSession.builder.appName("group_by_fans").master("local").config(
        #     conf=SparkConf()).getOrCreate()
        # self.sql_context = SQLContext(sparkContext=self.spark.sparkContext)
        # self.start_time = "2017-08-01 00:00"  # "publish_time": "2017-02-22 19:20"
        # self.time_format = "%Y-%m-%d %H:%M"
        # prod
        self.spark = SparkSession.builder.config(
            conf=SparkConf().setAppName("weibo_user_summary")).getOrCreate()
        self.sql_context = SQLContext(sparkContext=self.spark.sparkContext)
        self.days_list = self.dateRange("2017-10-16", "2017-10-21")
        self.path = 'hdfs:///ssymmetry_db/raw_db/sina_weibo_fans/sina_weibo_fans_item/2017/%s/*'
        self.output = '/home/spark/hxkTest/out/'

    def dateRange(self, begin_date, end_date):
        dates = []
        dt = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        date = begin_date[:]
        while date <= end_date:
            dates.append(date)
            dt = dt + datetime.timedelta(1)
            date = dt.strftime("%Y-%m-%d")
        return dates

    def read_dataframe(self, path, time_list):
        data_path = []
        for each_day in time_list:
            data_path.append(path % each_day)
        dataframe = self.spark.read.json(data_path)
        # local test
        # dataframe = self.spark.read.json("sina_weibo_fans_data_2017-11-09-10-18.json")
        return dataframe

    def read_blog_data(self, dataframe):
        df = dataframe.filter("blog_id is not NULL").select('uid', 'blog_content',
                                                            'forward_content').drop_duplicates().fillna(" ")
        return df

    def main(self):
        stop_words = []

        def user_tag_to_num(x):
            uid = x["uid"]
            user_tag = x["user_tag"]
            if user_tag == u"电视剧" or user_tag == u"电台" or user_tag == u"电影" or user_tag == u"动漫" \
                    or user_tag == u"广播电台" or user_tag == u"媒体传播" \
                    or user_tag == u"媒体人" or user_tag == u"美女模特" \
                    or user_tag == u"美女帅哥" or user_tag == u"休闲娱乐" \
                    or user_tag == u"娱乐明星" or user_tag == u"综艺":
                user_tag_num = 1
            elif user_tag == u"动物萌宠" or user_tag == u"萌宠":
                user_tag_num = 2
            elif user_tag == u"法律":
                user_tag_num = 3
            elif user_tag == u"房产":
                user_tag_num = 4
            elif user_tag == u"搞笑" or user_tag == u"搞笑幽默":
                user_tag_num = 5
            elif user_tag == u"互联网":
                user_tag_num = 6
            elif user_tag == u"健身" or user_tag == u"运动健身":
                user_tag_num = 7
            elif user_tag == u"教育" or user_tag == u"公益":
                user_tag_num = 8
            elif user_tag == u"科学":
                user_tag_num = 9
            elif user_tag == u"理财" or user_tag == u"投资理财":
                user_tag_num = 10
            elif user_tag == u"历史":
                user_tag_num = 11
            elif user_tag == u"旅游" or user_tag == u"旅游出行":
                user_tag_num = 12
            elif user_tag == u"美食":
                user_tag_num = 13
            elif user_tag == u"美妆":
                user_tag_num = 14
            elif user_tag == u"汽车" or user_tag == u"交通":
                user_tag_num = 15
            elif user_tag == u"社会时政" or user_tag == u"军事" or user_tag == u"政府政务" or user_tag == u"时事":
                user_tag_num = 16
            elif user_tag == u"数码":
                user_tag_num = 17
            elif user_tag == u"体育" or user_tag == u"体育竞技" or user_tag == u"游戏":
                user_tag_num = 18
            elif user_tag == u"养生" or user_tag == u"医疗" or user_tag == u"医疗健康" or user_tag == u"育儿":
                user_tag_num = 19
            elif user_tag == u"作家" or user_tag == u"艺术" or user_tag == u"音乐" or user_tag == u"收藏" or user_tag == u"设计" or user_tag == u"摄影" or user_tag == u"时尚":
                user_tag_num = 20
            elif user_tag == u"职场":
                user_tag_num = 21
            elif user_tag == u"宗教":
                user_tag_num = 22
            elif user_tag == u"星座命理" or user_tag == u"情感" or user_tag == u"婚庆":
                user_tag_num = 23
            elif user_tag == u"商界名人":
                user_tag_num = 24
            else:
                user_tag_num = 0

            return (uid, user_tag_num)

        # prod
        dataframe = self.read_dataframe(self.path, self.days_list).persist()
        blog_df = self.read_blog_data(dataframe)

        # read approved user list
        df = self.spark.read.csv(
            "hdfs:///ssymmetry_db/raw_db/sina_user_tag/sina_user_tag_item/weibo_uid_with_user_tag.csv", header=True) \
            .select("uid", "user_tag")

        user_tag_num_df = self.sql_context.createDataFrame(df.rdd.map(user_tag_to_num), ["uid", "user_tag"])

        # local test
        # dataframe = self.spark.read.json("sina_weibo_fans_data_2017-11-09-10-18.json")
        # blog_df = self.read_blog_data(dataframe).fillna(" ")
        # blog_rdd = blog_df.rdd

        # select the blogs for the tagged users
        tagged_user_blog = blog_df.join(user_tag_num_df, blog_df.uid == user_tag_num_df.uid).select(blog_df.uid,
                                                                                                    blog_df.blog_content,
                                                                                                    blog_df.forward_content,
                                                                                                    user_tag_num_df.user_tag)

        def preprocess_data(x):
            uid = x["uid"]
            blog_content = x["blog_content"]
            forward_content = x["forward_content"]
            user_tag = x["user_tag"]
            if forward_content.rfind(u"*****") > 0:
                forward_content = forward_content.split(u"*****")[1]
            return (uid, (blog_content + forward_content, user_tag))

        def extract_keywords(x):
            uid = x[0]
            # prod
            # ja.set_stop_words("/home/spark/hxkTest/movie_data/stopwords_cn.txt")
            ja.set_stop_words("/home/spark/hxkTest/spark_script/weibo_user_summary/stopwords_cn.txt")

            # local test
            # ja.set_stop_words("stopwords_cn.txt")

            keywords = ja.extract_tags(x[1][0])
            user_tag = x[1][1]
            return (uid, (keywords, user_tag))

        # the rdd contains uid, keywords and the user_tag, next step we need to convert the keywords to a matrix
        data = tagged_user_blog.rdd.map(preprocess_data).reduceByKey(lambda x, y: (x[0] + y[0], x[1])).map(
            extract_keywords).collect()

        uid_list = []
        keywords_list = []
        user_tag_list = []
        for elem in data:
            user_keyword = ""
            uid_list.append(elem[0])
            for word in elem[1][0][:-1]:
                user_keyword += word
                user_keyword += "_"
            user_keyword += elem[1][0][-1]
            keywords_list.append(user_keyword)
            user_tag_list.append(elem[1][1])

        result_dict = {"uid": uid_list, "keywords": keywords_list, "user_tag": user_tag_list}
        pd.DataFrame(result_dict, index=None).to_csv("/home/spark/hxkTest/spark_script/weibo_user_summary/tagged_user_keyword.csv")


if __name__ == "__main__":
    a = UserSummary()
    a.main()
