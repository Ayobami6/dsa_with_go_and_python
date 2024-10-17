#!/usr/bin/python3
"""
Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
"""


def str_str(haystack: str, needle: str) -> int:
    sub = ""
    n = len(haystack) - len(needle) + 1
    i = 0
    while i < n:
        for j in range(len(needle)):
            if haystack[i + j] == needle[j]:
                sub += haystack[i + j]

        if sub == needle:
            return i
        sub = ""
        i += 1
    return -1


haystack = "leetcode"
needle = "leeto"

print(str_str(haystack, needle))
