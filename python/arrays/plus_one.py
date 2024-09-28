#!/usr/bin/python3

from typing import List
"""
You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

# brute force  approact


def plus_one(digits: List[int]) -> List[int]:
    result_list = []
    str_list = []
    for d in digits:
        str_list.append(str(d))
    str_num = "".join(str_list)
    large_num = int(str_num) + 1
    back_to_str = str(large_num)
    for c in back_to_str:
        result_list.append(int(c))
    return result_list


# logical approach

def plus_one2(digits: List[int]) -> List[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    return [0] + digits


digits = [1, 2, 3]

print(plus_one(digits))
