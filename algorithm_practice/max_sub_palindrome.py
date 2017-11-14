# encoding=utf-8
'''
    Given a string S, find the longest palindromic substring in S.
    You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

    求字符串的最长回文子串
'''


def max_sub_palindrome(string_p):
    if len(string_p) <= 1:
        return string_p

    max_len = 0
    start = 0
    str_len = len(string_p)
    # 对于偶数长度的回文子串
    for i in range(1, str_len):
        low = i - 1
        high = i
        while low >= 0 and high < str_len and string_p[low] == string_p[high]:
            low -= 1
            high += 1
        if high - low - 1 > max_len:
            max_len = high - low - 1
            start = low + 1

    # 对于奇数长度的回文子串
    for i in range(1, str_len):
        low = i - 1
        high = i + 1
        while low >= 0 and high < str_len and string_p[low] == string_p[high]:
            low -= 1
            high += 1
        if high - low - 1 > max_len:
            max_len = high - low - 1
            start = low + 1
    return string_p[start:start + max_len]


print max_sub_palindrome("edcabcbacde")



#Method 2: Manacher算法，时间复杂度O(n), 空间复杂度O(n)
def pre_process(seq):
  res = ['#{}'.format(elem) for elem in seq]
  res.append('#$')
  res.insert(0,'^')
  return ''.join(res)

def manacher(seq):
  T = pre_process(seq)
  P = [0]*len(T)
  c,r = 0,0
  for i in range(1,len(T)):
    i_mirror = 2*c - i
    if r > i:
      P[i] = min(r-i, P[i_mirror])
    else:
      P[i] = 0
    while i+1+P[i] < len(T)-1 and i-1-P[i] >=0 and T[ i+1+P[i] ] == T[ i-1-P[i] ]:
      P[i] += 1
    if i + P[i] > r:
      c = i
      r = i+P[i]
  return max(P)

print manacher("edcabcbacde")