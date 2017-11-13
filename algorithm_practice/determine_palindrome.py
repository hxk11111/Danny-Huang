# encoding=utf-8
'''
    回文，英文palindrome，指一个顺着读和反过来读都一样的字符串，比如madam、我爱我，
    这样的短句在智力性、趣味性和艺术性上都颇有特色，中国历史上还有很多有趣的回文诗。
    那么，我们的第一个问题就是：判断一个字串是否是回文？
'''


def determine_palindrome(string_p):
    if len(string_p) <= 1:
        return True

    start = 0
    end = len(string_p) - 1
    flag = True
    while start < end:
        if flag and string_p[start] != string_p[end]:
            flag = False
        start += 1
        end -= 1
    return flag

print determine_palindrome("madam")
