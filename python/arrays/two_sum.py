#!/usr/bin/python3
from typing import List
"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one 
solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def two_sum(nums: List[int], target: int) -> List[int]:
    hold: dict = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hold:
            return [i, hold[diff]]

        hold[nums[i]] = i
    return []


nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))
