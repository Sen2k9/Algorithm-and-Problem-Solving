"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...

Example 1:

Input: 1
Output: "A"

Example 2:

Input: 28
Output: "AB"

Example 3:

Input: 701
Output: "ZY"
"""


class Solution:
    def convertToTitle(self, n: int):
        # Solution 1: fastest
        # res = ""

        # while n >= 1:
        #     rem = int(n % 26)
        #     n = n // 26
        #     print(n, rem)
        #     if rem == 0:
        #         res = "Z"+res
        #     else:
        #         res = chr(rem + 64) + res
        #     if rem == 0:
        #         n = n-1

        # return res
        # Solution 2:

        res = ""

        while n > 0:
            rem = int((n - 1) % 26)
            n = (n-1) // 26
            res = chr(rem + ord("A")) + res
        return res


sol = Solution()
n = 701
print(sol.convertToTitle(n))
