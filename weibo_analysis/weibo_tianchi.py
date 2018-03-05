# -*- coding: utf-8 -*-
# @Time    : 05/03/2018 11:21 PM
# @Author  : Huang_xk
# @FileName: weibo_tianchi.py

import pandas as pd
import numpy as np

# Read the train data, and retrieve the shape of training examples
train_data_df = pd.read_table("/Users/HUANG/Downloads/Weibo Data/weibo_train_data.txt", delimiter="\t",
                              names=("uid", "mid", "time", "forward_count", "comment_count", "like_count", "content"))
train = train_data_df.groupby("uid")
print train.size()
print train_data_df.shape

# Read the test data, and retrieve the shape of testing examples
test_data_df = pd.read_table("/Users/HUANG/Downloads/Weibo Data/weibo_predict_data.txt", delimiter="\t",
                              names=("uid", "mid", "time", "content"))
test = test_data_df.groupby("uid")
print test.size()
print test_data_df.shape

# Count the uids, which both contains in the training set and the testing set
print np.intersect1d(np.array(list(train_data_df["uid"])), np.array(list(test_data_df["uid"]))).shape
