# encoding=utf-8
'''
    单词翻转。输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变，句子中单词以空格符隔开。
    为简单起见，标点符号和普通字母一样处理。
    例如，输入“I am a student.”，则输出“student. a am I”
'''


def words_rotate(sentence):
    words_list = sentence.split(" ")
    start = 0
    end = len(words_list) - 1
    while start < end:
        words_list[start], words_list[end] = words_list[end], words_list[start]
        start += 1
        end -= 1
    return " ".join(words_list)


print words_rotate("I am a student.")
