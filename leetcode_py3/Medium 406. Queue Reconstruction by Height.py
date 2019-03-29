# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/3/22
File:   Medium 406. Queue Reconstruction by Height.py
"""
from typing import List

'''
Suppose you have a random list of people standing in a queue. 
Each person is described by a pair of integers (h, k), 
where h is the height of the person and k is the number of people in front of this person 
who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sorted_queue = sorted(people, key=lambda x: (-x[0], x[1]))
        result = []
        for item in sorted_queue:
            cnt = item[1]
            result.insert(cnt, item)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
