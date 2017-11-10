# encoding=utf-8
'''
定义字符串的左旋转操作：把字符串前面的若干个字符移动到字符串的尾部，如把字符串abcdef左旋转2位得到字符串cdefab。
请实现字符串左旋转的函数，要求对长度为n的字符串操作的时间复杂度为O(n)，空间复杂度为O(1)。
'''

'''
解法：
    1、对于字符串abc def ghi gk，将abc右移到def ghi gk后面，此时n = 11，m = 3，m’ = n % m = 2;abc def ghi gk -> def ghi abc gk
    2、问题变成gk左移到abc前面，此时n = m’ + m = 5，m = 2，m’ = n % m 1; abc gk -> a gk bc
    3、问题变成a右移到gk后面，此时n = m’ + m = 3，m = 1，m’ = n % m = 0; a gk bc-> gk a bc。 由于此刻，n % m = 0，满足结束条件，返回结果。

    即从左至右，后从右至左，再从左至右，如此反反复复，直到满足条件，返回退出。
'''


def str_rotate(str, head, tail, n, m, flag):
    # n 待处理部分的字符串长度，m：待处理部分的旋转长度
    # head：待处理部分的头指针，tail：待处理部分的尾指针
    # flag = true进行左旋，flag = false进行右旋
    if head == tail or m <= 0:
        return str

    if flag == True:
        # 进行左旋
        p1 = head
        p2 = p1 + m
        k = n - m - (n % m)
        while k > 0:
            temp = str[p1]
            str[p1] = str[p2]
            str[p2] = temp
            p1 += 1
            p2 += 1
            k -= 1
        str_rotate(str, p1, tail, m + n % m, n % m, False)
    else:
        # 进行右旋
        p1 = tail
        p2 = tail - m
        k = n - m - (n % m)
        while k > 0:
            temp = str[p1]
            str[p1] = str[p2]
            str[p2] = temp
            p1 -= 1
            p2 -= 1
            k -= 1
        str_rotate(str, head, p1, m + n % m, n % m, True)


str = ["a","b","c","d","e","f","g","h","i","j","k"]
i = 3
length = len(str)
str_rotate(str, 0, length-1, length, 3, True)
print(str)
