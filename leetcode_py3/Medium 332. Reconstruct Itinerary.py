# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/22
File:   Medium 332. Reconstruct Itinerary.py
"""
'''
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], 
reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. 
Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest 
lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller 
lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.

Example 1:
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:
Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
'''


class Solution:
    def findItinerary(self, tickets: 'List[List[str]]') -> 'List[str]':
        sorted_tickets = sorted(tickets)
        from_to_dict = dict()
        for from_p, to_p in sorted_tickets[::-1]:
            if from_p in from_to_dict:
                from_to_dict[from_p].append(to_p)
            else:
                from_to_dict[from_p] = [to_p]

        route = []
        start = "JFK"

        def dfs(airport):
            while airport in from_to_dict and from_to_dict[airport]:
                dfs(from_to_dict[airport].pop())
            route.append(airport)

        dfs(start)
        return route[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
