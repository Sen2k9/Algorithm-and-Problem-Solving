"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

"""


class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        # Solution 1: self
        # if len(s) < 2:
        #     return s
        # i = 0
        # j = len(s) - 1
        # while i <= j:
        #     temp = s[j]
        #     s[j] = s[i]
        #     s[i] = temp

        #     i += 1
        #     j -= 1
        #     print(s)
        # return s

        # Solution 2: self, fastest but not accepted in coding interview
        # s[::] = s[::-1]
        # return s

        # Solution 3:
        i = 0
        j = len(s) - 1
        while i <= j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
            # print(s)


sol = Solution()
s = ["h", "e", "l", "l", "o"]
print(sol.reverseString(s))
"""
corner case:
1. copying an input is not an solution
https://leetcode.com/problems/reverse-string/discuss/332519/Python-1-line-Do-not-return-anything-(greater99-Solutions)
"""
