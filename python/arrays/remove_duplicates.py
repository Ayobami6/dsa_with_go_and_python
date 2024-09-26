#!/usr/bin/python3

from typing import List
"""
Remove Duplicates from sorted array inplace
Given an integer array nums sorted in non-decreasing order, remove the 
duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you 
need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in 
the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""


def remove_duplicates(nums: List[int]) -> int:
    # let's use the first element in the array as our unique start pointer
    unique = 0
    # we'll check if the elements in array are unique by checking if the current item and the following next are not
    # same to determine if they are the same so we can proceed and incerement our unique value
    for i in range(len(nums)):
        # if the current element not equal to the next element, then the element are unique
        if nums[i] != nums[unique]:
            nums[unique + 1] = nums[i]
            # increment unique
            unique += 1
    return unique + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

print(remove_duplicates(nums))
