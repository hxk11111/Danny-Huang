# -*- coding: utf-8 -*-
# @Time    : 22/12/2017 10:24 PM
# @Author  : Huang_xk
# @FileName: dp_concat_2strs.py

# 输入三个字符串s1、s2和s3，判断第三个字 符串s3是否由前两个字符串s1和s2交错而成，即不改变s1和s2中各个字符原有的相对顺序.
# 例如当s1=“aabcc”，s2=“dbbca”，s3=“aadbbcbcac”时，则输出true，但如果 s3=“accabdbbca”，则输出false。

# 该问题可以转化为一个动态规划问题，用dp[i,j]表示s3[0:i+j]是由s1[0:i]和s2[0:j]转化而来，
# 若想问题结果为True，则s3[0]必须是s1[0] or s2[0], 然后再去做动态规划


def dp_concat_2strs(str1, str2, str3):
    s1_len = len(str1)
    s2_len = len(str2)
    s3_len = len(str3)
    # 如果s3的长度不等于s1和s2的长度之和，直接返回false
    if s3_len != s1_len + s2_len:
        return False

    dp_l = [[0 for _ in range(s1_len + 1)] for _ in range(s2_len + 1)]
    dp_l[0][0] = True
    for i in range(s1_len + 1):
        for j in range(s2_len + 1):
            if (i - 1 >= 0 and str1[i - 1] == str3[i + j - 1] and dp_l[j][i - 1]) or (
                    j - 1 >= 0 and str2[j - 1] == str3[i + j - 1] and dp_l[j - 1][i]):
                dp_l[j][i] = True
            elif i - 1 >= 0 or j - 1 >= 0:
                dp_l[j][i] = False
            else:
                pass
    return dp_l[s2_len][s1_len]


str1 = "aabcc"
str2 = "dbbca"
str3 = "aadbbcbcac"
print dp_concat_2strs(str1, str2, str3)
