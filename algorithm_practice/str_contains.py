# encoding=utf-8

'''
    假设这有一个各种字母组成的字符串A，和另外一个字符串B，字符串里B的字母数相对少一些。
    什么方法能最快的查出所有小字符串B里的字母在大字符串A里都有？
        比如，如果是下面两个字符串：
        String 1: ABCDEFGHLMNOPQRS
        String 2: DCGSRQPO
        答案是true，所有在string2里的字母string1也都有。
'''


# 方法一：先对两个字符串进行排序，在进行比较
class StringContains():
    def quick_sort(self, string_p):
        if len(string_p) <= 1:
            return string_p
        refer = string_p[0]
        less = ""
        greater = ""
        count_equal = 1
        str_length = len(string_p)
        for i in range(1, str_length):
            if refer < string_p[i]:
                greater += string_p[i]
            elif refer == string_p[i]:
                count_equal += 1
            else:
                less += string_p[i]
        return self.quick_sort(less) + refer * count_equal + self.quick_sort(greater)

    def str_contains(self, str_long, str_short):
        # 先对两个字符串排序
        long_string = self.quick_sort(str_long)
        short_string = self.quick_sort(str_short)
        long_pos = 0
        short_pos = 0
        while long_pos < len(str_long) and short_pos < len(str_short):
            while long_string[long_pos] < short_string[short_pos] and long_pos < len(long_string) - 1:
                long_pos += 1
            if long_string[long_pos] != short_string[short_pos]:
                break
            short_pos += 1

        if short_pos == len(str_short):
            return True
        else:
            return False


# a = StringContains()
# print a.str_contains("ABCDEFGHLMNOPQRS", "DCGSRQPOZ")


# 方法二：用素数相乘的方法
class StringContainsM2():
    def string_contains(self, str_long, str_short):
        prime_num = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
                     61, 67, 71, 73, 79, 83, 89, 97, 101]
        product = 1
        for i in range(len(str_long)):
            index = ord(str_long[i]) - ord("A")
            product *= prime_num[index]

        count = 0
        for j in range(len(str_short)):
            index_s = ord(str_short[j]) - ord("A")
            res = product % prime_num[index_s]
            if res != 0:
                break
            count += 1

        if count == len(str_short):
            return True
        else:
            return False


a = StringContainsM2()
print a.string_contains("ABCDEFGHLMNOPQRS", "DCGSRQPOL")
