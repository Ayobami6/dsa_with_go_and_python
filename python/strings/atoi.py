#!/usr/bin/python3
"""
Ascii to integer
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', 
assuming positivity is neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is 
encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], 
then round the integer to remain in the range. Specifically, 
integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.
"""


def atoi(s: str) -> int:
    # remove whitespaces
    s = s.strip()
    if not s:
        return 0
    idx = 0
    n = len(s)
    result = ""
    sign = 1

    if s[idx] == "-" or s[idx] == "+":
        sign = -1 if s[idx] == "-" else 1
        idx += 1

    while idx < n and s[idx].isdigit():
        result += s[idx]
        idx += 1

    if result != "":
        int_result = int(result)
    else:
        int_result = 0

    # handle overflow
    if int_result >= (2 ** 31):
        return int((2 ** 31) - 1) if sign == 1 else int(-2 ** 31)

    return int_result * sign


def myAtoi(self, s: str) -> int:
    s = s.strip()
    if not s:
        return 0

    sign = 1
    result = 0
    index = 0
    n = len(s)

    # Check the sign
    if s[index] == '-' or s[index] == '+':
        sign = -1 if s[index] == '-' else 1
        index += 1

    # Convert the characters to integers
    while index < n and s[index].isdigit():
        result = result * 10 + int(s[index])
        index += 1

        # Check for overflow
        if result >= 2**31:
            return -2**31 if sign == -1 else 2**31 - 1

    return result * sign


s = "0-1"
print(atoi(s))
