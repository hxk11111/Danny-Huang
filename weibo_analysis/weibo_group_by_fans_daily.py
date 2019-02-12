from pyspark.sql import SparkSession
from pyspark import SparkConf
import pandas as pd
import time
from datetime import timedelta
import datetime
from numpy import array
import calendar


class GroupByFans(object):
    def __init__(self):
        # local test
        # self.spark = SparkSession.builder.appName("group_by_fans").master("local").config(
        #     conf=SparkConf()).getOrCreate()
        # self.start = "2017-08-01 00:00"  # "publish_time": "2017-02-22 19:20"
        # self.time_format = "%Y-%m-%d %H:%M"
        # prod
        self.spark = SparkSession.builder.appName("group_by_fans_daily").config(
            conf=SparkConf().setAppName("group_by_fans_daily")).getOrCreate()
        this_monday = datetime.date.today()
        if this_monday == calendar.MONDAY:
            self.start = (this_monday - timedelta(days=14))
        else:
            one_day = datetime.timedelta(days=1)
            while this_monday.weekday() != calendar.MONDAY:
                this_monday -= one_day
            self.start = (this_monday - timedelta(days=7))
        self.time_format = "%Y-%m-%d %H:%M"
        self.start_time = self.start.strftime(self.time_format)  # "publish_time": "2017-02-22 19:20"
        end = datetime.datetime.strptime(self.start_time, self.time_format) + timedelta(days=7)
        self.end_time = end.strftime(self.time_format)
        self.yesterday = (datetime.date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        self.path = 'hdfs:///ssymmetry_db/raw_db/sina_weibo_fans/sina_weibo_fans_item/2017/%s/*'
        self.output = '/home/spark/hxkTest/out/'

    def read_dataframe(self, path, time):
        dataframe = self.spark.read.json(path % time)
        return dataframe

    def read_data(self, dataframe):
        # rdd = self.spark.read.json(self.path % self.yesterday).filter("blog_id is not NULL and fans != 'None'") \
        #     .select('uid', 'fans', 'publish_time', 'praise', 'repeat', 'forward').rdd
        start = self.start_time
        end = self.end_time
        rdd = dataframe.filter(
            'blog_id is not NULL and fans != "None" and publish_time > "%s" and publish_time < "%s"' % (start, end)) \
            .select('uid', 'fans', 'publish_time', 'praise', 'repeat', 'forward').rdd
        # local test
        # rdd = self.spark.read.json("/Users/hxk11111/Desktop/script/test.txt").filter(
        #     "blog_id is not NULL and fans != 'None'") \
        #     .select('uid', 'fans', 'publish_time', 'praise', 'repeat', 'forward').rdd
        return rdd

    def read_distinct(self, dataframe):
        rdd = dataframe.filter("fans != 'None'") \
            .select('uid', 'fans').rdd.distinct()
        # local test
        # rdd = self.spark.read.json("/Users/hxk11111/Desktop/script/test.txt").filter(
        #     "blog_id is not NULL and fans != 'None'") \
        #     .select('uid', 'fans').rdd.distinct()
        return rdd

    def main(self):

        # def time_filter(x):
        #     publish_time = x["publish_time"]
        #     # Calculate the time 7 days after start_time
        #     end_time = (
        #         datetime.datetime.strptime(self.start_time, self.time_format) + timedelta(days=7)).strftime(
        #         self.time_format)
        #     # for item in time_list:
        #     if (publish_time > self.start_time and publish_time < end_time):
        #         return True
        #     else:
        #         return False

        def info_parse(x, y):
            # Calculate the number of fans, the sum of the praises/forwards/repeats and the time list for a user
            total_fans = x[1]
            # print(total_fans)
            total_praise = x[2] + y[2]
            total_repeat = x[3] + y[3]
            total_forward = x[4] + y[4]
            pub_time_list = x[0] + y[0]
            return (pub_time_list, total_fans, total_praise, total_repeat, total_forward)

        def add_group_tag(x):
            # After reduceByKey by the last step, the result has the format of key=uid, value=list
            uid = x[0]
            info_list = x[1]
            total_weibo = len(info_list[0])
            total_praise = info_list[2]
            total_repeat = info_list[3]
            total_forward = info_list[4]
            fans_num = info_list[1]
            # print(fans_num)
            if fans_num <= 100:
                return (0, (total_weibo, total_praise, total_repeat, total_forward, 1))
            # add the subs for different ranges
            for i in range(9):
                # Generate a list of [2,3,4,5,6], to construct the power
                for j in range(2, 7):
                    if (fans_num > (i + 1) * 10 ** j) and (fans_num <= (i + 2) * 10 ** j):
                        return ((i + 1) * 10 ** j, (total_weibo, total_praise, total_repeat, total_forward, 1))
                    if fans_num > 10 ** 7:
                        return (10 ** 7, (total_weibo, total_praise, total_repeat, total_forward, 1))

        def detail_parse(x, y):
            # The total number of users whose fans number lies in a specific range
            user_nums = x[4] + y[4]

            # The total number of praise of these users
            total_praise_by_fans = x[1] + y[1]
            total_repeat_by_fans = x[2] + y[2]
            total_forward_by_fans = x[3] + y[3]
            total_weibo_by_fans = x[0] + y[0]

            return (total_weibo_by_fans, total_praise_by_fans, total_repeat_by_fans, total_forward_by_fans, user_nums)

        dataframe = self.read_dataframe(self.path, self.yesterday).persist()
        rdd = self.read_data(dataframe)
        # Firstly, convert the rdd to a tuple format data, key is 'uid', value is the information we need
        # Secondly, use reduceByKey to group the data by uid, calculate the total number of weibo posted, and some other infomation
        # Then, categorize the data by the fans the user has
        # Finally, calculate the total number of users in each group
        # start_time = self.start
        # paired_rdd = rdd.filter(lambda x: x["publish_time"].encode("utf-8").decode("unicode_escape") > start_time
        #                                   and x["publish_time"].encode("utf-8").decode("unicode_escape") <
        #                                       (datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M") + timedelta(
        #                                           days=7))
        #                         .strftime("%Y-%m-%d %H:%M")).map(lambda x: (
        #     x["uid"], ([x["publish_time"]], int(x["fans"]),
        #                0 if (x["praise"] == u"\u8d5e" or x["praise"] is None) else int(x["praise"]),
        #                0 if (x["repeat"] == u"\u8bc4\u8bba" or x["repeat"] is None) else int(x["repeat"]),
        #                0 if (x["forward"] == u"\u8f6c\u53d1" or x["forward"] is None) else int(
        #                    x["forward"])))).reduceByKey(info_parse).map(add_group_tag).reduceByKey(
        #     detail_parse).sortByKey().collect()
        paired_rdd = rdd.map(lambda x: (
            x["uid"], ([x["publish_time"]], int(x["fans"]),
                       0 if (x["praise"] == u"\u8d5e" or x["praise"] is None) else int(x["praise"]),
                       0 if (x["repeat"] == u"\u8bc4\u8bba" or x["repeat"] is None) else int(x["repeat"]),
                       0 if (x["forward"] == u"\u8f6c\u53d1" or x["forward"] is None) else int(
                           x["forward"])))).reduceByKey(info_parse).map(add_group_tag) \
            .reduceByKey(detail_parse).sortByKey().collect()

        # Create dataframes for .csv files.
        fans_group_list = []
        fans_num_list = []
        total_weibo_list = []
        total_praises = []
        total_repeats = []
        total_forwards = []
        for each in paired_rdd:
            fans_group_list.append(each[0])
            fans_num_list.append(each[1][4])
            total_weibo_list.append(each[1][0])
            total_praises.append(each[1][1])
            total_repeats.append(each[1][2])
            total_forwards.append(each[1][3])

        def group_tag_for_all(x):
            fans_number = x[1]
            # print(fans_number)
            if fans_number <= 100:
                return (0, 1)
            # add the subs for different ranges
            for i in range(9):
                # Generate a list of [2,3,4,5,6], to construct the power
                for j in range(2, 7):
                    if (fans_number > (i + 1) * 10 ** j) and (fans_number <= (i + 2) * 10 ** j):
                        return ((i + 1) * 10 ** j, 1)
                    if fans_number > 10 ** 7:
                        return (10 ** 7, 1)

        # Calculate the number of accounts in different groups, including the accounts posted or didn't post weibos last week
        fans_rdd = self.read_distinct(dataframe)
        user_total_by_fans = []
        fans_num_rdd = fans_rdd.map(lambda x: (x["uid"], int(x["fans"]))).reduceByKey(lambda x,y: x).map(group_tag_for_all).reduceByKey(lambda x, y: x + y).sortByKey().collect()
        for item in fans_num_rdd:
            user_total_by_fans.append(item[1])

        # Calculate the average number of weibos posted by different groups. Using total_num_weibo_posted / total_num_users
        # weibo_arr = array(total_weibo_list)
        # user_arr = array(user_total_by_fans)
        # avg_weibo = (weibo_arr / user_arr).tolist()
        fans_num_df = pd.DataFrame(
            {
                "range": fans_group_list,
                "total number of users posted": fans_num_list,
                "total number of users": user_total_by_fans,
                "z total weibo posted": total_weibo_list,
                "z total praises": total_praises,
                "z total repeats": total_repeats,
                "z total forwards": total_forwards
            }
        )
        fans_num_df.to_csv(self.output + "fans_num_%s_daily.csv" % self.yesterday, index=None)
        # fans_num_df.to_csv("fans_num.csv", index=None)


if __name__ == "__main__":
    a = GroupByFans()
    a.main()
