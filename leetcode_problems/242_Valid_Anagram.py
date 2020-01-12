"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

"""


class Solution:
    def isAnagram(self, s, t):
        # Solution 1: self
        # s = sorted(s)
        # t = sorted(t)
        # if s == t:
        #     return True
        # return False

        # Solution 2: slower
        # if len(s) != len(t):
        #     return False
        # dic = {}
        # for each in s:
        #     if each not in dic:
        #         dic[each] = 1
        #     else:
        #         dic[each] += 1
        # for each in t:
        #     if dic.get(each, 0) == 0:
        #         return False
        #     else:
        #         dic[each] -=1
        # return True

        # Solution 3: slower
        # if len(s) != len(t):
        #     return False

        # for each in s:
        #     if each in t:
        #         t= t.replace(each,"",1)
        #     else:
        #         return False

        #     print(each,t)

        # #print(t)
        # if not t:
        #     return True
        # return False

        # Solution 4: fastest
        import collections

        dic = collections.defaultdict(int)

        for each in s:
            dic[each] += 1
            
        for each in t:
            dic[each] -= 1
            
        for each in dic.values():
            if each != 0:
                return False
        return True

        

sol = Solution()
s = "aacc"
t = "ccac"
print(sol.isAnagram(s,t))

"""
https://en.wikipedia.org/wiki/Anagram

corner case:
"aacc"
"ccac"

"""
