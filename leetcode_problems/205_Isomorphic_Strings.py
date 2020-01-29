"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

Note:
You may assume both s and t have the same length.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str):
        # Solution 1: self, inefficient
        # from collections import Counter
        # dic_s = {}
        # dic_t = {}
        # for i in range(len(s)):
        #     if s[i] in dic_s:
        #         dic_s[s[i]].append(i)
        #     else:
        #         dic_s[s[i]] = [i]
        # for i in range(len(t)):
        #     if t[i] in dic_t:
        #         dic_t[t[i]].append(i)
        #     else:
        #         dic_t[t[i]] = [i]
        # for i in range(len(s)):
        #     #print(dic_s[s[i]], dic_t[t[i]])
        #     if dic_s[s[i]] != dic_t[t[i]]:
        #         return False

        # return True

        # Solution 2: very efficient and clever

        z = zip(s, t)
        # print(set(z))
        return len(set(z)) == len(set(s)) == len(set(t))


sol = Solution()
s = "foo"
t = "bar"
print(sol.isIsomorphic(s, t))
