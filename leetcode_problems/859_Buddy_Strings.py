"""
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.
Example 1:

Input: A = "ab", B = "ba"
Output: true

Example 2:

Input: A = "ab", B = "ab"
Output: false

Example 3:

Input: A = "aa", B = "aa"
Output: true

Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true

Example 5:

Input: A = "", B = "aa"
Output: false

Note:

    0 <= A.length <= 20000
    0 <= B.length <= 20000
    A and B consist only of lowercase letters.
"""


class Solution:
    def buddyStrings(self, A: str, B: str):
        import functools

        if(len(A) != len(B)):
            return False

        X = list(filter(lambda x: x[0] != x[1], zip(A, B)))
        count = len(X)
        print(X)
        print(X[0][::-1])

        if (count == 2 and X[0][::-1] == X[1]):
            return True
        elif (count == 0):
            if len(A) > len(set(A)):  # for all same characters
                return True

        return False


sol = Solution()
A = "aaaaaaabc"
B = "aaaaaaacb"

print(sol.buddyStrings(A, B))
