"""
Assume you have a method isSubstring which checks if one word is a substring of another.
Given two string s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring
(e.g., "waterbottle" is a rotation of "erbottlewat")
"""


class Solution:
    def stringRotation(self, s1, s2):
        if len(s1) != len(s2) or len(s1) < 1:
            return False

        return self.substring(s1 + s1, s2)

    def substring(self, s1s1, s2):

        i = 0
        j = len(s2)
        #print(s1s1, s2)

        while i <= len(s1s1)//2:

            if s1s1[i] == s2[0]:
                #print(s1s1[i: i+j])
                if s1s1[i: i+j] == s2:
                    return True

            i += 1

        return False

        #     letters = list(s1)
        #     new_arr = []

        #     for i in range(len(letters)):

        #         new_arr = letters[i + 1:] + letters[: i + 1]

        #         if self.match(new_arr, list(s2)):
        #             return True

        #     return False

        # def match(self, new_arr, target):

        #     return new_arr == target  # O(n)


sol = Solution()
s1 = "waterbottle"
s2 = "erbottlewat"
print(sol.stringRotation(s1, s2))
