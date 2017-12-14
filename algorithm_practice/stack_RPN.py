# -*- coding: utf-8 -*-
# @Time    : 10/12/2017 7:17 PM
# @Author  : Huang_xk
# @FileName: stack_RPN.py

# 逆波兰表达式Reverse Polish Notation，又叫后缀表达式
# 中缀表达式:a+(b-c)*d  后缀表达式:abc-d*+

def stack_RPN(string_p):
    stack = []
    length = len(string_p)
    for i in range(length):
        if string_p[i].isdigit():
            stack.append(string_p[i])
        else:
            if string_p[i] == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num1) + int(num2))
            elif string_p[i] == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2) - int(num1))
            elif string_p[i] == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2) * int(num1))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2) / int(num1))

    return stack.pop()

print stack_RPN("21+3*")
print stack_RPN(["4", "13", "5", "/", "+"])