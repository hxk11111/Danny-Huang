# encoding=utf-8
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

# 提取特征词
def words_dict(all_words_list, deleteN):
    feature_words = []
    n = 1
    for i in range(deleteN, len(all_words_list)):
        if n > 5000:
            break
        if not all_words_list[i].isdigit():
            feature_words.append(all_words_list[i])
            n += 1
    return feature_words

# 文本特征
def text_features(train_data_list, test_data_list, feature_words):
    def text_features(text, feature_words):
        text_words = set(text)
        features = [1 if word in text_words else 0 for word in feature_words]
        return features
    train_feature_list = [text_features(text, feature_words) for text in train_data_list]
    test_feature_list = [text_features(text, feature_words) for text in test_data_list]
    return train_feature_list, test_feature_list


df = pd.read_csv("tagged_user_keyword.csv")
keywords = list(df["keywords"])
uid_list = list(df["uid"])
keywords_list = []
for elem in keywords:
    keywords_list.append(str(elem).decode("utf-8").split("_")[:-1])
user_tag_list = list(df["user_tag"])
# 将样本数据划分训练集和测试集
train_data_list, test_data_list, train_class_list, test_class_list = train_test_split(
    keywords_list, user_tag_list, test_size=0.2)
# 统计词频放入all_words_dict
all_words_dict = {}
for word_list in keywords_list:
    for word in word_list:
        if all_words_dict.has_key(word):
            all_words_dict[word] += 1
        else:
            all_words_dict[word] = 1
# key函数利用词频进行降序排序
all_words_tuple_list = sorted(all_words_dict.items(), key=lambda f:f[1], reverse=True)
all_words_list = list(zip(*all_words_tuple_list)[0])
deleteNs = range(0, 1000, 200)
for deleteN in deleteNs:
    feature_words = words_dict(all_words_list, deleteN)
    print ">>>>>>>Setting up Lists for Multinomial Naive Bayes Model with deleteN : %d" % deleteN
    train_feature_list, test_feature_list = text_features(train_data_list, test_data_list, feature_words)
    print ">>>>>>>Training Set Shape: ", len(train_feature_list)
    print ">>>>>>>Testing Set Shape: ", len(test_feature_list)
    print ">>>>>>>Building Model"
    classifier = MultinomialNB().fit(train_feature_list, train_class_list)
    label_list = classifier.predict(test_feature_list)
    test_accuracy = classifier.score(test_feature_list, test_class_list)
    df = pd.DataFrame(
        {
            "predicted_label": label_list,
            "actual label": test_class_list
        }
    )
    df.to_csv("predict_res_%d.csv" % deleteN)
    print "test_accuracy with deleteN %d is : " % deleteN, test_accuracy
