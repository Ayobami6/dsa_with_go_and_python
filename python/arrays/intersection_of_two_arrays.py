#!/usr/bin/python3
from typing import List
"""
Intersection of two arrays
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as 
many times as it shows in both arrays and you may return the result in any order.
"""


def intersection_of_arrays(nums1: List[int], nums2: List[int]) -> List[int]:
    result = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                nums2.pop(j)
                break
    return result


# nums1 = [1, 2, 2, 1]

# nums2 = [2]
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print(intersection_of_arrays(nums1, nums2))
