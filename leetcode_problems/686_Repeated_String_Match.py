"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").
Note:
The length of A and B will be between 1 and 10000.
"""


import math


class Solution:
    def repeatedStringMatch(self, A: str, B: str):
        from collections import Counter

        if not set(B).issubset(A):
            return - 1

        n = len(B)//len(A)

        for i in range(3):
            if B in A * (n + i):
                return n + i
        return -1


sol = Solution()
A = "abc"
B = "cabcabca"
print(sol.repeatedStringMatch(A, B))

#assert sol.repeatedStringMatch(A, B) == 3
