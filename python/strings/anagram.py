#!/usr/bin/python3
"""
Given two strings s and t, 
return true if t is an anagram of s, and false otherwise.
"""


def is_anagram(s: str, t: str) -> bool:
    # store the frequency of the s
    if len(s) != len(t):
        return False
    store: dict = {}
    for i in range(len(s)):
        if s[i] in store:
            # increment store
            store[s[i]] += 1
        else:
            store[s[i]] = 1

    # check if all characters in t has the same freq as s
    for i in range(len(t)):
        if t[i] in store:
            store[t[i]] -= 1
        else:
            return False

    values = store.values()
    if max(values) == 0:
        return True
    else:
        return False
