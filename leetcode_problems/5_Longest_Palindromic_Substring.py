"""
Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"

"""
import unittest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        ans = ""

        start = 0

        for start in range(len(s)):
            # for odd string "aba"
            temp = self.helper(s, start, start)

            if len(temp) > len(ans):
                ans = temp
            # for even string "abba"
            temp = self.helper(s, start, start + 1)
            if len(temp) > len(ans):
                ans = temp
        return ans

    def helper(self, s, start, end):

        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start + 1:end]


class TestSuite(unittest.TestCase):
    def test_palindrome(self):
        sol = Solution()
        self.assertEqual(sol.longestPalindrome("babad"), "bab")
        self.assertEqual(sol.longestPalindrome("cbbd"), "bb")


if __name__ == "__main__":
    unittest.main()

"""
Time complexity : O(n^2)
Space complexity : O(1)
"""