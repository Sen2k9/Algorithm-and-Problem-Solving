"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1

Example 2:

Input: 16
Output: true
Explanation: 24 = 16

Example 3:

Input: 218
Output: false
"""


class Solution:
    def isPowerOfTwo(self, n: int):
        if n < 0:
            return False
        s = bin(n & 0xffffffff).replace("0b", "")
        # print(s)
        return s.count("1") == 1


sol = Solution()
n = -2147483648

print(sol.isPowerOfTwo(n))
