"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""


class Solution:
    def addBinary(self, a: str, b: str):
        # solution 1: self
        c = 0
        result = ""
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 and j >= 0:
            c, d = divmod(c + int(a[i]) + int(b[j]), 2)
            result = str(d) + result
            i -= 1
            j -= 1
        while i >= 0:
            c, d = divmod(c + int(a[i]), 2)
            i -= 1
            result = str(d) + result
        while j >= 0:
            c, d = divmod(c + int(b[j]), 2)
            j -= 1
            result = str(d) + result
        if c:
            return str(c) + result

        return result

        # Solution 2: not recommended but faster

        return bin(int(a, 2)+int(b, 2)).replace("0b", "")


sol = Solution()
a = "1010"
b = "10"
print(sol.addBinary(a, b))
