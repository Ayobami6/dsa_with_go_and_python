#!/usr/bin/python3

from typing import List
"""
Rotate Array
Steps:
set two pointer to for left and right
swap left and rights until they are equal
"""


def rotate_array(nums: List[int], k: int) -> List[int]:
    left = 0
    right = len(nums) - 1

    # first flip
    while left < right:
        tmp = nums[left]
        nums[left] = nums[right]
        nums[right] = tmp
        left += 1
        right -= 1

    # second flip
    n = len(nums)
    k = k % n
    left = 0
    right = k - 1
    while left < right:
        tmp = nums[left]
        nums[left] = nums[right]
        nums[right] = tmp
        left += 1
        right -= 1

    # third flip
    left = k
    right = len(nums) - 1
    while left < right:
        tmp = nums[left]
        nums[left] = nums[right]
        nums[right] = tmp
        left += 1
        right -= 1
    return nums


nums = [1, 2, 3, 4, 5, 6, 7]

print(rotate_array(nums, 3))
