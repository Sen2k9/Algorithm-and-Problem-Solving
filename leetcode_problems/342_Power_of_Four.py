"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true

Example 2:

Input: 5
Output: false

Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfFour(self, num: int):
        # Solution 1: self
        if num < 0:
            return False

        s = bin(num).replace("0b", "")
        # number power of 4 has total odd number of bits with only 1 bit

        if s.count("1") == 1:
            if len(s) % 2 == 1:
                return True
            else:
                return False
        else:
            return False
