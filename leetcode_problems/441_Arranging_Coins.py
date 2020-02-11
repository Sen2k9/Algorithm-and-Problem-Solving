"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.

Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
"""


class Solution:
    def arrangeCoins(self, n: int):
        # Solution 1: self
        # if n < 2:
        #     return n
        # coins = n
        # for i in range(1, n + 1):
        #     if i > coins:
        #         return i - 1
        #     coins -= i

        # Solution 2: using math, fastest
        import math
        return int((-1+math.sqrt(1+8*n))/2)


sol = Solution()
n = 10
print(sol.arrangeCoins(n))

"""
corner case:
1. n = 1
2. n = 0

references:
https://en.wikipedia.org/wiki/Quadratic_formula
https://leetcode.com/problems/arranging-coins/discuss/453240/Python3%3A-one-liner-Math-solution-explained
"""
