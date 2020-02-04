"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true

Example 2:

Input: 14
Output: false

"""


class Solution:
    def isPerfectSquare(self, num: int):
        # Solution 1: brute-force
        # i = 1

        # while i*i <= num:
        #     if i*i == num:
        #         return True
        #     i += 1

        # return False
        # Solution 2: faster, using binary search

        if num == 1:
            return num
        i = 1
        j = num - 1

        while i <= j:
            mid = (i + j) // 2

            if mid * mid > num:
                j = mid - 1
            elif mid * mid < num:
                i = mid + 1

            else:
                return True
        return False


sol = Solution()
num = 1
print(sol.isPerfectSquare(num))
