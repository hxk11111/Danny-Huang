# encoding=utf-8
'''输入一个整形数组，数组里有正数也有负数。
数组中连续的一个或多个整数组成一个子数组，每个子数组都有一个和。
求所有子数组的和的最大值。要求时间复杂度为O(n)。
例如输入的数组为1, -2, 3, 10, -4, 7, 2, -5，和最大的子数组为3, 10, -4, 7, 2，
因此输出为该子数组的和18。'''


def max_sublist(list):
    cur = 0
    length = len(list)
    sum_num = 0
    max_num = 0
    while cur < length:
        sum_num += list[cur]
        cur += 1
        if sum_num < 0:
            sum_num = 0
        elif sum_num > max_num:
            max_num = sum_num
    return max_num


l = [1, -2, 3, 10, -4, 7, 2, -5]
print max_sublist(l)
