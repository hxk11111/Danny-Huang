# encoding=utf-8
import numpy as np
from sklearn.model_selection import train_test_split
import pickle
import pandas as pd


# convert the keywords list to a matrix
def text_to_index_array(model_dict, keywords_list):
    keywords = []
    for word in keywords_list:
        try:
            keywords.append(model_dict[word])
        except:
            keywords.append(0)
    return np.array(keywords)


# 读取大的语料文本
print ">>>>>>>读取pickle文件，并反序列化"
file = open("/udisk2/hxk/w2vec/w2vec.pkl", "rb")
index_dict = pickle.load(file)
word_vectors = pickle.load(file)
new_dict = index_dict

print ">>>>>>>Setting up Arrays for Keras Embedding Layer"
n_symbols = len(index_dict) + 1
embedding_weights = np.zeros((n_symbols, 128))  # 创建一个n_symbols * 128的0矩阵
for w, index in index_dict.items():
    embedding_weights[index, :] = word_vectors[w]  # 词向量矩阵，第一行是0向量

# read csv file which contains uid, keywords and the user_tag
data = pd.read_csv("/home/spark/hxkTest/spark_script/weibo_user_summary/tagged_user_keyword.csv", header=0)
keywords = list(data["keywords"])
user_tag = list(data["user_tag"])

# 划分训练和测试数据集
X_train_l, X_test_l, y_train_l, y_test_l = train_test_split(keywords, user_tag, test_size=0.2)



# todo: 将X_train和X_test转换成matrix