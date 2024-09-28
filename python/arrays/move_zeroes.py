#!/usr/bin/python3

from typing import List
"""
Given an integer array nums, move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""


def move_zeros(nums: List[int]) -> List[int]:
    left: int = 0
    right: int = 0

    while right < len(nums):
        if nums[right] != 0:
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left += 1
        right += 1
    return nums


nums = [0, 1, 0, 3, 12]

print(move_zeros(nums))
