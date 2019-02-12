from pyspark.sql import SparkSession
from pyspark import SparkConf
import pandas as pd
import time
from datetime import timedelta
import datetime
from numpy import array
import calendar


class WeiboUserTag(object):
    def __init__(self):
        # local test
        # self.spark = SparkSession.builder.appName("group_by_fans").master("local").config(
        #     conf=SparkConf()).getOrCreate()
        # self.start = "2017-08-01 00:00"  # "publish_time": "2017-02-22 19:20"
        # self.time_format = "%Y-%m-%d %H:%M"
        # prod
        self.spark = SparkSession.builder.config(
            conf=SparkConf().setAppName("weibo_user_tag")).getOrCreate()
        self.path = 'hdfs:///ssymmetry_db/raw_db/sina_user_tag/sina_user_tag_item/2017/%s/*'
        self.output = '/home/spark/hxkTest/out/'
        self.days_list = ["2017-10-20", "2017-10-21", "2017-10-23", "2017-10-24", "2017-10-25"]

    def dateRange(self, begin_date, end_date):
        dates = []
        dt = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        date = begin_date[:]
        while date <= end_date:
            dates.append(date)
            dt = dt + datetime.timedelta(1)
            date = dt.strftime("%Y-%m-%d")
        return dates

    def read_dataframe(self, path, days_list):
        data_path = []
        for elem in days_list:
            data_path.append(path % elem)
        dataframe = self.spark.read.json(data_path)
        rdd = dataframe.filter('user_tag is not NULL')\
            .select('uid', 'user_tag').rdd
        # local test
        # rdd = self.spark.read.json("/Users/hxk11111/Desktop/script/test.txt").filter(
        #     "blog_id is not NULL and fans != 'None'") \
        #     .select('uid', 'fans', 'publish_time', 'praise', 'repeat', 'forward').rdd
        return rdd

    def main(self):

        rdd = self.read_dataframe(self.path, self.days_list)
        # dataframe = self.spark.read.json("sina_user_tag_data_2017-10-24-16-22.json")
        # rdd = dataframe.filter('user_tag is not NULL').select('uid', 'user_tag').rdd

        result = rdd.map(lambda x:(x["user_tag"], 1)).reduceByKey(lambda x,y: x + y).collect()

        user_tag_list = []
        user_num = []
        total = 0
        for item in result:
            user_tag_list.append(item[0])
            user_num.append(item[1])
            total += item[1]
        result_dict = {"user_tag_list":user_tag_list, "user_num":user_num}
        print total

        df = pd.DataFrame(result_dict)
        df.to_csv("sina_user_tag_result.csv", encoding="utf-8")

if __name__ == "__main__":
    a = WeiboUserTag()
    a.main()
