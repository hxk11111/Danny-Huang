# encoding=utf-8
# Longest Common Subsequence,LCS

# m,n分别为list1和list2的标志位，b和c均为二元数组，b用来存放方向信息，c用来存放LCS的长度
def LCS(m, n, list1, list2, b, c):
    for i in range(1, m):
        for j in range(1, n):
            if list1[i - 1] == list2[j - 1]:
                b[i][j] = "equal"
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                if c[i][j - 1] > c[i - 1][j]:
                    b[i][j] = "left"
                    c[i][j] = c[i][j - 1]
                else:
                    b[i][j] = "up"
                    c[i][j] = c[i - 1][j]


def get_LCS(i, j, list1, list2, b):
    if i == 0 or j == 0:
        return
    if b[i][j] == "equal":
        get_LCS(i - 1, j - 1, list1, list2, b)
        print list1[i - 1]
    elif b[i][j] == "left":
        get_LCS(i, j - 1, list1, list2, b)
    else:
        get_LCS(i - 1, j, list1, list2, b)


list1 = "bcefac"
list2 = "aefaec"
m = len(list1) + 1
n = len(list2) + 1
b = [[0 for _ in range(n)] for _ in range(m)]
c = [[0 for _ in range(n)] for _ in range(m)]
LCS(m, n, list1, list2, b, c)
get_LCS(m - 1, n - 1, list1, list2, b)
