# -*- coding: utf-8 -*-
# @File  : str_KMP_correct.py
# @Author: Huang_xk
# @Date  : 12/9/17

def compute_next(string_p):
    length = len(string_p)
    next_l = [0]
    for i in range(1, length):
        inter_list = []
        sub_str = string_p[:i + 1]
        sub_len = len(sub_str)
        str_pre = set(sub_str[:j] for j in range(1, sub_len))
        str_back = set(sub_str[k:] for k in range(sub_len - 1, 0, -1))
        inter_list += list(str_pre.intersection(str_back))
        if len(inter_list) == 0:
            next_l.append(0)
        else:
            next_l.append(max([len(item) for item in inter_list]))
    return next_l


print compute_next("ABCABCABCD")
