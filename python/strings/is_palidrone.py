#!/usr/bin/python
import re
"""
A phrase is a palindrome if, after converting all uppercase letters 
into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""


def is_palidrone(s: str) -> bool:
    # strip s for whitespaces

    lower: str = s.lower()
    # pattern for sub
    pattern: str = r'[^a-z0-9]'
    cleaned_s = re.sub(pattern, '', lower)
    p1 = 0
    p2 = len(cleaned_s) - 1
    while p1 < p2:
        if cleaned_s[p1] != cleaned_s[p2]:
            return False
        p1 += 1
        p2 -= 1

    return True


def isPalindrone(s: str) -> bool:
    lower = s.lower()
    # pattern for sub
    pattern = r'[^a-z0-9]'
    stripped_text = re.sub(pattern, '', lower)
    reverse = stripped_text[::-1]
    if reverse == stripped_text:
        return True
    else:
        return False


s = "A man, a plan, a canal: Panama"

print(is_palidrone(s))
