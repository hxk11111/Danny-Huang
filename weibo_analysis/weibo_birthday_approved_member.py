from pyspark.sql import SparkSession
from pyspark import SparkConf
import pandas as pd
import time
from datetime import timedelta
import datetime
from numpy import array
import re


class GroupByFans(object):
    def __init__(self):
        # local test
        # self.spark = SparkSession.builder.appName("group_by_fans").master("local").config(
        #     conf=SparkConf()).getOrCreate()
        # self.start_time = "2017-08-01 00:00"  # "publish_time": "2017-02-22 19:20"
        # self.time_format = "%Y-%m-%d %H:%M"
        # prod
        self.spark = SparkSession.builder.appName("group_by_fans_weekly").config(
            conf=SparkConf().setAppName("weiboUser_birthday_icon")).getOrCreate()
        self.start = (datetime.date.today() - timedelta(days=15))
        self.time_format = "%Y-%m-%d %H:%M"
        self.start_time = self.start.strftime(self.time_format)  # "publish_time": "2017-02-22 19:20"
        end = datetime.datetime.strptime(self.start_time, self.time_format) + timedelta(days=7)
        self.end_time = end.strftime(self.time_format)
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

    def read_data(self, dataframe):
        # rdd = self.spark.read.json(self.path % self.today).filter("blog_id is not NULL and fans != 'None'") \
        #     .select('uid', 'fans', 'publish_time', 'praise', 'repeat', 'forward').rdd
        rdd = dataframe.filter(
            'forward_content is NULL and fans != "None" and icon_approve is not NULL') \
            .select('uid', 'fans').drop_duplicates().rdd
        # local test
        # rdd = self.spark.read.json("/Users/huangxiangkai/Desktop/script/test.txt").filter(
        #     "blog_id is not NULL and fans != 'None'") \
        #     .select('uid', 'fans', 'publish_time', 'praise', 'repeat', 'forward').rdd
        return rdd


    def main(self):

        def add_group_tag(x):
            # After reduceByKey by the last step, the result has the format of key=uid, value=list
            uid = x["uid"]
            fans_num = int(x["fans"])
            # print(fans_num)
            if fans_num <= 100:
                return (0, (uid, fans_num))
            # add the subs for different ranges
            for i in range(9):
                # Generate a list of [2,3,4,5,6], to construct the power
                for j in range(2, 7):
                    if (fans_num > (i + 1) * 10 ** j) and (fans_num <= (i + 2) * 10 ** j):
                        return ((i + 1) * 10 ** j, (uid, fans_num))
                    if fans_num > 10 ** 7:
                        return (10 ** 7, (uid, fans_num))

        dataframe = self.read_dataframe(self.path, self.days_list).persist()
        rdd = self.read_data(dataframe)

        paired_rdd = rdd.map(add_group_tag).collect()

        # Create dataframes for .csv files.
        fans_group_list = []
        uid_list = []
        fans_num_list = []
        for each in paired_rdd:
            fans_group_list.append(each[0])
            uid_list.append(each[1][0])
            fans_num_list.append(each[1][1])

        fans_num_df = pd.DataFrame(
            {
                "range": fans_group_list,
                "uid": uid_list,
                "fans_num": fans_num_list,
            }
        )


        def filter_birthday(x):
            birthday = x["birthday"]
            pattern = re.match(ur"\d+\u5e74\d+\u6708\d+\u65e5", birthday)
            if pattern:
                # print(pattern.group())
                return 1
            else:
                return 0

        birthday_rdd = dataframe.filter('birthday is not NULL').select("birthday").rdd
        count = birthday_rdd.map(filter_birthday).reduce(lambda x,y: x+y)
        print count


        fans_num_df.to_csv(self.output + "weibo_birthday_and_approved_member.csv", index=None)
        # fans_num_df.to_csv("fans_num.csv", index=None)


if __name__ == "__main__":
    a = GroupByFans()
    a.main()
