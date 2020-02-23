"""
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true

Example 2:

Input: 0
Output: false

Example 3:

Input: 9
Output: true

Example 4:

Input: 45
Output: false

Follow up:
Could you do it without using any loop / recursion?
"""


class Solution:
    def isPowerOfThree(self, n: int):
        # if n <= 0:
        #     return False
        # if n == 1:
        #     return True

        # while n % 3 == 0:
        #     #print(n, n % 3)

        #     n = n / 3
        #     if abs(n) == 1:
        #         return True
        # return False

        # Solution 2:
        if n <= 0:
            return False
        import math
        power = round(math.log(n, 3))
        # print(power)
        return 3**power == n


sol = Solution()
n = 1
print(sol.isPowerOfThree(n))
"""
reference:
https://leetcode.com/problems/power-of-three/discuss/440072/Python-Time%3A-O(log(n))-95.8-Space%3A-O(1)-100.0-General-Range-Solution-Clean-Code
"""
