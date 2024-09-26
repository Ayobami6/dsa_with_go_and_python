#!/usr/bin/python3

from typing import List
"""
Contains duplicate 
Given an integer array nums, return true if any value appears 
at least twice in the array, and return false if every element is distinct.
using my strategy pattern `Seen before`


"""


def contain_duplicates(nums: List[int]) -> bool:
    hold = {}
    for i in range(len(nums)):
        if nums[i] in hold:
            return True
        hold[nums[i]] = i

    return False


nums = [1, 2, 3, 4]
print(contain_duplicates(nums=nums))
