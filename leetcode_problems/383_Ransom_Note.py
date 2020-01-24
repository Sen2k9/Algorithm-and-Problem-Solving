"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str):
        # Solution 1:self
        # if len(magazine) < len(ransomNote):
        #     return False
        # dic = {}
        # for each in magazine:
        #     dic[each] = dic.get(each, 0) + 1
        # for each in ransomNote:
        #     if dic.get(each, 0):
        #         dic[each] -= 1
        #     else:
        #         return False
        # return True

        # Solution 2:self, fastest
        for each in ransomNote:
            if each in magazine:
                magazine = magazine.replace(each, "", 1)
            else:
                return False

        return True


sol = Solution()
r = ""
m = "a"
print(sol.canConstruct(r, m))
"""
corner case:
1.ransomNote can be empty
"""
