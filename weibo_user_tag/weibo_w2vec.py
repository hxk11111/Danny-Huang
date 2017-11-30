#encoding=utf-8
from pyspark.sql import SparkSession
from pyspark import SparkConf, SQLContext
import datetime
import jieba
from pyspark.ml.feature import Word2Vec
import pickle


class Weibo_Word2Vec(object):
    def __init__(self):
        # local test
        # self.spark = SparkSession.builder.appName("group_by_fans").master("local").config(
        #     conf=SparkConf()).getOrCreate()
        # self.start_time = "2017-08-01 00:00"  # "publish_time": "2017-02-22 19:20"
        # self.time_format = "%Y-%m-%d %H:%M"
        # prod
        self.spark = SparkSession.builder.config(
            conf=SparkConf().setAppName("weibo_w2vec")).getOrCreate()
        self.days_list = self.dateRange("2017-10-16", "2017-11-21")
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
        df = dataframe.filter("blog_id is not NULL").select('uid', 'blog_content', 'forward_content').drop_duplicates()
        return df

    def main(self):
        stop_words = []
        # prod
        dataframe = self.read_dataframe(self.path, self.days_list).persist()

        # read approved user list
        # df = self.spark.read.csv(
        #     "hdfs:///ssymmetry_db/raw_db/sina_user_tag/sina_user_tag_item/weibo_uid_with_user_tag.csv")\
        #     .select("uid", "user_tag")

        # local test
        # dataframe = self.spark.read.json("sina_weibo_fans_data_2017-11-09-10-18.json")

        blog_rdd = self.read_blog_data(dataframe).fillna(" ").rdd

        def preprocess_data(x):
            uid = x["uid"]
            blog_content = x["blog_content"]
            forward_content = x["forward_content"]
            if forward_content.rfind(u"*****") > 0:
                forward_content = forward_content.split(u"*****")[1]
            return (uid, blog_content + forward_content)

        data = blog_rdd.map(preprocess_data).reduceByKey(lambda x, y: x + y).map(
            lambda x: [" ".join(jieba.cut(x[1])).split(" ")])

        sql_context = SQLContext(sparkContext=self.spark.sparkContext)
        word_df = sql_context.createDataFrame(data, ["values"])

        w2vec = Word2Vec(vectorSize=128, inputCol="values")
        model = w2vec.fit(word_df)

        def creat_dictionary(model):
            w_df = model.getVectors()
            w_df.show()
            data = w_df.rdd.collect()
            w2index = {}
            w2vec = {}
            i = 1
            for row in data:
                word = row.word
                vector = row.vector
                w2index[word] = i
                w2vec[word] = vector
                i += 1
            return w2index, w2vec

        # 把word2vec的词向量写出到一个pickle文件中
        index_dict, word_vectors = creat_dictionary(model)
        # out = open("w2vec.pkl", "wb")
        out = open("/udisk2/hxk/w2vec/w2vec.pkl", "wb")
        pickle.dump(index_dict, out)  # 索引字典
        pickle.dump(word_vectors, out)  # 词向量字典
        out.close()

        # test
        model.findSynonyms("你", 3).show()


if __name__ == "__main__":
    a = Weibo_Word2Vec()
    a.main()
    # print("text")
