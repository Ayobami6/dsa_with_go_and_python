#!/usr/bin/python3
from typing import List

"""

Write a function to find the longest common prefix 
string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


def longest_common_prefix(strs: List[str]) -> str:
    prefix = strs[0]
    for item in strs[1::]:
        while not item.startswith(prefix):
            prefix = prefix[:-1]

    if not prefix:
        return ""
    else:
        return prefix


strs = ["flower", "flow", "flight"]

print(longest_common_prefix(strs))
