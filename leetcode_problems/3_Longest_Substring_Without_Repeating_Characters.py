"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
import unittest


class Solution:

    def __init__(self):
        pass

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = set()
        ans = 0
        ptr1 = 0
        ptr2 = 0
        n = len(s)
        while ptr1 < n and ptr2 < n:
            if s[ptr2] not in seen:
                seen.add(s[ptr2])
                ptr2 += 1
                ans = max(ans, ptr2 - ptr1)
            
            else:
                seen.remove(s[ptr1])
                ptr1 += 1
        return ans


class TestSuite(unittest.TestCase):

    def test_lengthOfLongestSubstring(self):

        sol = Solution()

        # self.assertEqual(sol.lengthOfLongestSubstring("bbbbb"), 1)
        # self.assertEqual(sol.lengthOfLongestSubstring(""), 0)
        self.assertEqual(sol.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(sol.lengthOfLongestSubstring("dvdf"), 3)
        self.assertEqual(sol.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(sol.lengthOfLongestSubstring("anviaj"), 5)


if __name__ == '__main__':
    unittest.main()
