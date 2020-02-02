"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
Note:
    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution:
    def addStrings(self, num1: str, num2: str):
        # Solution 1: self
        # O(n)
        # O(1)
        i = len(num1)-1
        j = len(num2)-1
        c = 0
        ans = ""

        while i >= 0 and j >= 0:
            a = num1[i]
            b = num2[j]
            c, s = divmod(int(a)+int(b)+c, 10)

            i -= 1
            j -= 1

            ans = str(s) + ans
            # print(ans)

        while i >= 0:
            a = num1[i]
            c, s = divmod(int(a) + c, 10)
            i -= 1
            ans = str(s) + ans

        while j >= 0:
            b = num2[j]
            c, s = divmod(int(b) + c, 10)
            j -= 1
            ans = str(s) + ans
        if c > 0:
            return str(c)+ans
        return ans


sol = Solution()
a = "999"
b = "999"
print(sol.addStrings(a, b))

"""
corner case:
1. non-negative means 0
"""
