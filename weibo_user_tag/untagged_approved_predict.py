# encoding=utf-8
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
from sklearn.externals import joblib


# 提取特征词
def words_dict(all_words_list, deleteN):
    feature_words = []
    n = 1
    for i in range(deleteN, len(all_words_list)):
        if n > 4000:
            break
        if not all_words_list[i].isdigit():
            feature_words.append(all_words_list[i])
            n += 1
    return feature_words


# 文本特征
def text_features(train_data_list, feature_words):
    def text_features(text, feature_words):
        text_words = set(text)
        features = [1 if word in text_words else 0 for word in feature_words]
        return features

    train_feature_list = [text_features(text, feature_words) for text in train_data_list]
    return train_feature_list


df = pd.read_csv("tagged_user_keyword.csv")
keywords = list(df["keywords"])
uid_list = list(df["uid"])
keywords_list = []
for elem in keywords:
    key_list = str(elem).decode("utf-8").split("_")[:-1]
    if len(key_list) > 8:
        key_list = key_list[:9]
    keywords_list.append(key_list)
user_tag_list = list(df["user_tag"])
# 将样本数据划分训练集和测试集
# train_data_list, test_data_list, train_class_list, test_class_list = train_test_split(
#     keywords_list, user_tag_list, test_size=0.2)

# 统计词频放入all_words_dict
all_words_dict = {}
for word_list in keywords_list:
    for word in word_list:
        if all_words_dict.has_key(word):
            all_words_dict[word] += 1
        else:
            all_words_dict[word] = 1
# key函数利用词频进行降序排序
all_words_tuple_list = sorted(all_words_dict.items(), key=lambda f: f[1], reverse=True)
all_words_list = list(zip(*all_words_tuple_list)[0])

deleteN = 0
feature_words = words_dict(all_words_list, deleteN)
print ">>>>>>>Setting up Lists for Multinomial Naive Bayes Model with deleteN : %d" % deleteN
train_feature_list = text_features(keywords_list, feature_words)
print ">>>>>>>Training Set Shape: ", len(train_feature_list)
# print ">>>>>>>Testing Set Shape: ", len(test_feature_list)
print ">>>>>>>Building Model"
classifier = MultinomialNB().fit(train_feature_list, user_tag_list)

# 读取被预测的数据
df_predicted = pd.read_csv("untagged_approved_user_keyword.csv")
keywords_predicted_l = list(df_predicted["keywords"])
keywords_predicted = []
for elem in keywords_predicted_l:
    key_list = str(elem).decode("utf-8").split("_")[:-1]
    if len(key_list) > 8:
        key_list = key_list[:9]
    keywords_predicted.append(key_list)
uid_predicted = list(df_predicted["uid"])

predict_feature_list = text_features(keywords_predicted, feature_words)
label_list = classifier.predict(predict_feature_list)
# test_accuracy = classifier.score(test_feature_list, test_class_list)
label_list_cn = []
for label in label_list:
    if label == 0:
        label_list_cn.append("其他")
    elif label == 1:
        label_list_cn.append("影视娱乐")
    elif label == 2:
        label_list_cn.append("宠物")
    elif label == 3:
        label_list_cn.append("法律")
    elif label == 4:
        label_list_cn.append("房产")
    elif label == 5:
        label_list_cn.append("搞笑")
    elif label == 6:
        label_list_cn.append("互联网")
    elif label == 7:
        label_list_cn.append("健身")
    elif label == 8:
        label_list_cn.append("教育公益")
    elif label == 9:
        label_list_cn.append("科学")
    elif label == 10:
        label_list_cn.append("理财")
    elif label == 11:
        label_list_cn.append("历史")
    elif label == 12:
        label_list_cn.append("旅游")
    elif label == 13:
        label_list_cn.append("美食")
    elif label == 14:
        label_list_cn.append("美妆")
    elif label == 15:
        label_list_cn.append("汽车")
    elif label == 16:
        label_list_cn.append("时政军事")
    elif label == 17:
        label_list_cn.append("数码")
    elif label == 18:
        label_list_cn.append("体育游戏")
    elif label == 19:
        label_list_cn.append("医疗养生")
    elif label == 20:
        label_list_cn.append("文艺")
    elif label == 21:
        label_list_cn.append("职场")
    elif label == 22:
        label_list_cn.append("宗教")
    elif label == 23:
        label_list_cn.append("星座情感")
    else:
        label_list_cn.append("商界")

df = pd.DataFrame(
    {
        "uid": uid_predicted,
        "predicted_label": label_list_cn
    }
)
df.to_csv("untagged_predict_res.csv", index=False, encoding="utf-8")
# print "test_accuracy with deleteN %d is : " % deleteN, test_accuracy

# joblib.dump(classifier, "multi_nb_%d.model" % deleteN)
