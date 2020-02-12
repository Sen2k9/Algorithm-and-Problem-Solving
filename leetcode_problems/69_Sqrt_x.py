"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2

Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.

"""


class Solution:
    def mySqrt(self, x: int):
        # Solution 1:
        # Runtime : O(x^0.5)
        # if x < 1:
        #     return x
        # i = 1
        # while i * i <= x:
        #     i += 1
        # return i - 1

        # Solution 2: using binary search
        # Runtime : O(logx^0.5)
        i = 0
        j = x

        while i <= j:
            mid = (i + j) // 2
            if mid * mid > x:
                j = mid - 1
            elif mid * mid < x:
                i = mid + 1
            else:
                return mid
        return j


sol = Solution()
x = 10
print(sol.mySqrt(x))
"""
reference:
https://leetcode.com/problems/sqrtx/discuss/344755/Python-solution-with-binary-search
"""
