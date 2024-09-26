#!/usr/bin/python3

from typing import List
"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""


def single_number(nums: List[int]) -> int:
    hold: dict = {}
    for i in range(len(nums)):
        if nums[i] in hold:
            hold[nums[i]] += 1
        else:
            hold[nums[i]] = 1

    for k, v in hold.items():
        if v == 1:
            return k
    return -1


nums = [1]
print(single_number(nums))
