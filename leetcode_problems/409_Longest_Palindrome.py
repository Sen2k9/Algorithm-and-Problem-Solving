"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


class Solution:
    def longestPalindrome(self, s: str):
        # Solution 1: best solution
        from collections import Counter
        dic = Counter(s)
        one = False
        total = 0

        for _, v in dic.items():
            if not one and v % 2 == 1:
                one = True

            total += (v//2)*2

        return total if not one else total+1


sol = Solution()
s = "ccc"
print(sol.longestPalindrome(s))
