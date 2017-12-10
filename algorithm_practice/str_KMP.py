# encoding=utf-8
# KMP Algorithm
# 给定文本串text和模式串pattern，从文本串text中找出模 式串pattern第一次出现的位置

def next_list(str_p):
    longest = []
    i = len(str_p)
    for j in range(i / 2 + 1):
        if str_p[0:j] == str_p[i - j:i]:
            longest.append(j)
        else:
            continue
    return max(longest)


def next_list_m2(str_p):
    str_prefix = [str_p[0:i + 1] for i in range(len(str_p) - 1)]
    str_latfix = [str_p[i + 1:] for i in range(len(str_p) - 1)]
    common = list(set(str_latfix) & set(str_prefix))
    if len(common) == 0:
        return 0
    else:
        return max([len(item) for item in common])

str_p = "ABCABCABC"
print next_list_m2(str_p)


def KMP(str_l, str_s):
    flag = True
    index = 0
    j = 0
    while index < len(str_l) - len(str_s) + 1:
        while j < len(str_s):
            if str_l[index + j] == str_s[j]:
                flag = True
                j += 1
                continue
            if j:
                flag = False
                move = next_list_m2(str_s[:j])
                index = index + j - move
                j = move
                break
            else:
                flag = False
                index += 1
                break
        if flag:
            return True
    return False


str_l = "ABCABCABCABCD"
str_s = "ABCABCD"
print KMP(str_l, str_s)
