"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false

"""


class Solution:
    def isPalindrome(self, s: str):
        # Solution 1:self, slow

        # character = "abcdefghijklmnopqrstuvwxyz0123456789"
        # s = s.replace(" ", "")
        # l = list(s)
        # i = 0
        # j = len(l) - 1
        # # print(l)
        # while i < len(l) and j >= 0:
        #     # while instead of if to avoid multiple blank space and commas
        #     while i < len(l) and l[i].lower() not in character:
        #         i += 1
        #     while j >= 0 and l[j].lower() not in character:
        #         j -= 1
        #     #print(l[i], l[j])
        #     #print(i, j)

        #     if i < len(l) and j >= 0:
        #         if l[i].lower() != l[j].lower():
        #             return False
        #         else:
        #             i += 1
        #             j -= 1
        # return True

        # Solution 2: fastest, using regular expression
        import re
        s = re.sub(r'\W+', '', s)
        print(s)
        #s = s.replace(' ', '')
        print(s[::-1])
        if s.lower() == s[::-1].lower():
            return True
        return False


sol = Solution()
s = "race a car"
print(sol.isPalindrome(s))
"""
corner case:
1. string with only blanck space
2. alphanumeric
3. includes special characters

reference:
https://developers.google.com/edu/python/regular-expressions?csw=1
"""
