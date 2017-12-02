# encoding=utf-8
# Longest Increasing Subsequence
# 给定一个长度为N的数组,找出一个最长的 单调递增子序列。
# 例如:给定数组 {5, 6, 7, 1, 2, 8}, 则其最长的单调递增子序列为{5,6,7,8},长度为4。

def LIS(list_p):
    longest = [1 for _ in range(len(list_p))]
    longest_index = [[1]]
    for i in range(1, len(list_p)):
        index = []
        for j in range(i):
            if list_p[j] < list_p[i]:
                longest[i] += 1
                index.append(j)
        index.append(i)
        longest_index.append(index)
    return longest, longest_index


l1 = [1, 4, 5, 7, 3]
longest, longest_index = LIS(l1)
print longest
max_index = 0
for i in range(len(longest)):
    if longest[i] > max_index:
        max_index = i
for i in longest_index[max_index]:
    print l1[i]
