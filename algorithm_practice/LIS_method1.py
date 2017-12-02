# encoding=utf-8
# Longest Increasing Subsequence
# 给定一个长度为N的数组,找出一个最长的 单调递增子序列。
# 例如:给定数组 {5, 6, 7, 1, 2, 8}, 则其最长的单调递增子序列为{5,6,7,8},长度为4。



# 方法一：先对数组进行排序，然后再求两个数组的LCS
def quick_sort(list_p):
    if len(list_p) == 0:
        return list_p
    less = []
    large = []
    length = len(list_p)
    target = list_p[0]
    equal = 1
    for i in range(1, length):
        if list_p[i] > target:
            large.append(list_p[i])
        elif list_p[i] < target:
            less.append(list_p[i])
        else:
            equal += 1
    return quick_sort(less) + equal * [target] + quick_sort(large)


def LCS(m, n, list1, list2, b, c):
    for i in range(1, m):
        for j in range(1, n):
            if list1[i - 1] == list2[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "equal"
            elif c[i - 1][j] > c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "up"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "left"


def getLCS(m, n, list1, b):
    if m == 0 or n == 0:
        return
    if b[m][n] == "equal":
        getLCS(m - 1, n - 1, list1, b)
        print list1[m - 1]
    elif b[m][n] == "left":
        getLCS(m, n - 1, list1, b)
    else:
        getLCS(m - 1, n, list1, b)


list1 = [1, 4, 5, 7, 3]
list2 = quick_sort(list1)
m = len(list1) + 1
n = len(list2) + 1
b = [[0 for _ in range(n)] for _ in range(m)]
c = [[0 for _ in range(n)] for _ in range(m)]
LCS(m, n, list1, list2, b, c)
getLCS(m - 1, n - 1, list1, b)
