# encoding=utf-8
'''
    用欧几里得算法求最大公约数
'''


def max_common_divisor(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    if a % b == 0:
        max_divisor = b
        print max_divisor
    else:
        r = a % b
        max_common_divisor(r, b)


max_common_divisor(544, 119)
