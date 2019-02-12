from pyspark.sql import SparkSession
from pyspark import SparkConf
import pandas as pd
import time
import redis
from datetime import timedelta
import datetime
from numpy import array


class GroupByFans(object):
    def __init__(self):
        # local test
        self.spark = SparkSession.builder.appName("group_by_fans").master("local").config(
            conf=SparkConf()).getOrCreate()
        # self.start_time = "2017-08-01 00:00"  # "publish_time": "2017-02-22 19:20"
        # self.time_format = "%Y-%m-%d %H:%M"

        # prod
        # self.spark = SparkSession.builder.appName("remedy_weibo_first_week").config(
        #     conf=SparkConf()).getOrCreate()
        # self.start = (datetime.date.today() - timedelta(days=15))
        self.time_format = "%Y-%m-%d %H:%M"
        self.start_time = "2017-10-02 00:00"  # "publish_time": "2017-02-22 19:20"
        end = datetime.datetime.strptime(self.start_time, self.time_format) + timedelta(days=7)
        self.end_time = end.strftime(self.time_format)
        hdfs_start_time = self.end_time.split(" ")[0]
        hdfs_end_time = (datetime.datetime.strptime(hdfs_start_time, "%Y-%m-%d") + timedelta(days=2)).strftime(
            "%Y-%m-%d")
        self.days_list = self.dateRange(hdfs_start_time, hdfs_end_time)
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
        return dataframe

    def read_distinct(self, dataframe):
        rdd = dataframe.select('uid').rdd.distinct()
        return rdd

    def main(self):

        def f(x):
            server = redis.Redis(host="10.10.237.8", port=6379)
            redis_key = "remedy_weibo_1009_1012"
            print(x)
            for item in x:
                if item["uid"] is not None:
                    server.sadd(redis_key, item["uid"])

        dataframe = self.read_dataframe(self.path, self.days_list)
        # dataframe = self.read_dataframe(self.path, ["2017-08-21"])
        # dataframe = self.spark.read.json("/Users/hxk11111/Desktop/script/sina_weibo_fans_data_2017-09-14-01-50.json")
        rdd = self.read_distinct(dataframe).foreachPartition(f)

if __name__ == "__main__":
    a = GroupByFans()
    a.main()
