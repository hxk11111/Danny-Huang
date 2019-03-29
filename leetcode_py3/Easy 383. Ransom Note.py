# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/3/16
File:   Easy 383. Ransom Note.py
"""
'''
Given an arbitrary ransom note string and another string containing letters from all the magazines,
write a function that will return true if the ransom note can be constructed from the magazines ; 
otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn_list = [ch for ch in ransomNote]
        for ch in magazine:
            if ch in rn_list:
                rn_list.remove(ch)
        if len(rn_list) == 0:
            return True
        return False
