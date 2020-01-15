"""
 Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters. 
"""


class Solution:
    def firstUniqChar(self, s):
        # Solution 1: self, fastest

        from collections import Counter

        c = Counter(s)
        print(c)

        for key in c.keys():  # this is guranteed to be faster because Counter also maintain the order of insertion, user print to see the key,value pair
            if c[key] == 1:
                return s.index(key)
        return - 1


sol = Solution()
s = "loveleetcode"

print(sol.firstUniqChar(s))
"""
corner case:
"aadadaad"

"""
