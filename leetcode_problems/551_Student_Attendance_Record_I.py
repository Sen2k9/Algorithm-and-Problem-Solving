"""
You are given a string representing an attendance record for a student. The record only contains the following three characters:

    'A' : Absent.
    'L' : Late.
    'P' : Present.

A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:

Input: "PPALLP"
Output: True

Example 2:

Input: "PPALLL"
Output: False
"""


class Solution:
    def checkRecord(self, s: str):
        # Solution 1: self
        # dic = {"A": 1, "L": 1}
        # prev = ""
        # for each in s:
        #     if each == "A":
        #         if dic.get(each, 0):
        #             dic[each] -= 1
        #         else:
        #             return False
        #     elif each == "L" and prev == each:
        #         if dic.get(each, 0):
        #             dic[each] -= 1
        #         else:
        #             return False
        #     elif each == "L" and not prev == each:
        #         dic[each] = 1
        #     prev = each
        # return True

        # solution 2: using regx
        import re

        if re.search('LLL+', s):
            return False
        absent = 1
        for each in s:

            if each == "A":
                absent -= 1
            if absent == -1:
                return False
        return True


sol = Solution()
s = "PPALLP"
print(sol.checkRecord(s))
"""
corner case:
"LLPPPLL"
"""
