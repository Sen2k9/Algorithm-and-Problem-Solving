"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"

Example 2:

Input: "leetcode"
Output: "leotcede"

Note:
The vowels does not include the letter "y".
"""


class Solution:
    def reverseVowels(self, s):
        # Solution 1: self
        if len(s) < 2:
            return s
        i = 0
        j = len(s) - 1
        s = list(s)
        v = ["a","A","e","E","i","I","o","O","u","U"]
        while i <= j:
            if s[i] not in v:
                i += 1
            if s[j] not in v:
                j -= 1
            if i <= j and s[i] in v and s[j] in v:
                s[i], s[j] = s[j], s[i] # more pythonic
                # temp = s[j]
                
                # s[j] = s[i]
                # s[i] = temp
                i += 1
                j -= 1
            #print(s,s[i],s[j])
        return "".join(s)

        # Solution 2: using dictionary
        # if len(s) < 2:
        #     return s
 
        # s = list(s)
        # v = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
        # dic = {}

        # for i in range(len(s)):
        #     if s[i] in v:
        #         dic[i] = s[i]

        # #print(dic, dic.keys(),dic.values())
        # l = list(dic.keys())
        # l[:] = l[::-1]
        # l2 = list(dic.values())
        # #print(l,l2)

        # for i in range(len(l)):
        #     s[l[i]] = l2[i]
        # return "".join(s)

        

sol = Solution()
s = "race a car"
print(sol.reverseVowels(s))
        
"""
corner case:
string immutable
1. length of string less than 2
"""
