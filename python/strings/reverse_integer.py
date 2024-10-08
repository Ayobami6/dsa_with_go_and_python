#!/usr/bin/python3
"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

requires:
if reversed x is > 2 ** 31 return 0 
if reversed x is < -2 ** 31 return 0
check if negative or positve
if negative retain after reverse
"""


def reverse_integer(x: int) -> int:
    int_max = (2 ** 31) - 1
    int_min = -2 ** 31

    is_negative = x < 0

    if is_negative:
        # make positive
        x = x * -1
    reverse = int(str(x)[::-1])

    if is_negative:
        # back to negative
        reverse = reverse * -1

    if reverse > int_max or reverse < int_min:
        return 0

    return reverse


print(reverse_integer(-123))
