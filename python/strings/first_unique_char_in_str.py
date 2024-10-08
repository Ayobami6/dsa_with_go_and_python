#!/usr/bin/python
from collections import OrderedDict
"""
Given a string s, 
find the first non-repeating character in it 
and return its index. If it does not exist, return -1.
tools:
OrderDict Data structure
"""


def first_uniq_char(s: str) -> int:
    # create a new order dict instance
    order_dict: OrderedDict = OrderedDict()
    # loop through the char in the str
    for i in range(len(s)):
        if s[i] in order_dict:
            order_dict[s[i]] += 1
        else:
            order_dict[s[i]] = 1

    for i, char in enumerate(s):
        if order_dict[char] == 1:
            return i

    return -1
