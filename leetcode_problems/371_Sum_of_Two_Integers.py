"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3

Example 2:

Input: a = -2, b = 3
Output: 1
"""


class Solution:
    def getSum(self, a: int, b: int):
        while b:
            #print(bin(a), bin(b))
            tmp = a ^ b
            print(bin(tmp))
            b = (a & b) << 1
            print(bin(b))

            a = tmp & 0xffffffff
            print(bin(a))
            print(a >> 31)

            print(bin(a ^ 0xffffffff))
        return a if a >> 31 == 0 else ~(a ^ 0xffffffff)


sol = Solution()
a = -2
b = 3
print(sol.getSum(a, b))

"""
reference:
https://leetcode.com/problems/sum-of-two-integers/discuss/293945/one-python-solution-with-bit-manipulation
"""
