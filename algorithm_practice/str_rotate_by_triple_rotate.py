# encoding=utf-8

'''
    用三步翻转法做字符串的左旋
'''


def str_rotate_by_triple_rotate(str_list, m):
    str1 = str_list[0:m]
    str2 = str_list[m:]
    res = rotate(rotate(str1) + rotate(str2))
    return res


def rotate(string_list):
    start = 0
    end = len(string_list) - 1
    while start < end:
        temp = string_list[start]
        string_list[start] = string_list[end]
        string_list[end] = temp
        start += 1
        end -= 1
    return string_list


print str_rotate_by_triple_rotate("a,b,c,d,e,f,g,h".split(","), 3)
