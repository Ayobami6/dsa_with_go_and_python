#!/usr/bin/python3
from typing import List
"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""


def reverse_string(str: List[str]) -> List[str]:
    start = 0
    end = len(str) - 1

    while start < end:
        # swap
        str[start], str[end] = str[end], str[start]
        start += 1
        end -= 1
    return str


s = ["h", "e", "l", "l", "o"]

print(reverse_string(s))
