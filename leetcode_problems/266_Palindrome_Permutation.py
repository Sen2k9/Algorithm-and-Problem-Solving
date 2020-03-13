"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false

Example 2:

Input: "aab"
Output: true

Example 3:

Input: "carerac"
Output: true
"""


class Solution:
    def canPermutePalindrome(self, s: str):
        if s is None:
            return False
        s_dict = {}
        for letter in s:
            if letter not in s_dict:
                s_dict[letter] = 1
            else:
                s_dict[letter] += 1

        seen_odd = False

        for value in s_dict.values():
            if value % 2 == 1:
                if seen_odd == False:
                    seen_odd = True
                else:
                    return False

        return True


sol = Solution()
s = "code"
print(sol.canPermutePalindrome(s))
