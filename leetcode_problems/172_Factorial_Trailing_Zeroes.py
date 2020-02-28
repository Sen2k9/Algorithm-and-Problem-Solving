"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Note: Your solution should be in logarithmic time complexity.
"""


class Solution:
    def trailingZeroes(self, n: int):
        if n < 1:
            return 1
        count = 0
        while n:
            n = n // 5
            count = count + n
        return count


sol = Solution()
print(sol.trailingZeroes(25))

assert sol.trailingZeroes(0) == 1
assert sol.trailingZeroes(25) == 6
