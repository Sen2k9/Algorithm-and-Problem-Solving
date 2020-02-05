"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:

Input: "aba"
Output: False

Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""


class Solution:
    def repeatedSubstringPattern(self, s: str):
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                j = n // i
                print(s[:i]*j)
                if s[:i] * j == s:
                    return True
        return False


sol = Solution()
s = "abaababaab"

print(sol.repeatedSubstringPattern(s))
