"""
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

    Characters ('a' to 'i') are represented by ('1' to '9') respectively.
    Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.

Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

Example 2:

Input: s = "1326#"
Output: "acz"

Example 3:

Input: s = "25#"
Output: "y"

Example 4:

Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"

Constraints:

    1 <= s.length <= 1000
    s[i] only contains digits letters ('0'-'9') and '#' letter.
    s will be valid string such that mapping is always possible.

"""


class Solution:
    def freqAlphabets(self, s):
        # Solution 1: self, using list
        # i = len(s) - 1
        # n = []
        # while i >= 0:
        #     if s[i] == "#":
        #         n.append(chr(int(s[i - 2:i])+96)) # converting ascii number to character
        #         i = i - 3
        #     else:
        #         n.append(chr(int(s[i])+96))
        #         i = i - 1
        # return "".join(n[::-1])

        # Solution 2: self, using string concatenation, fastest
        i = len(s) - 1
        n = ""
        while i >= 0:
            if s[i] == "#":
                n = chr(int(s[i - 2:i])+96)+n
                i = i - 3
            else:
                n = chr(int(s[i])+96)+n
                i = i - 1
        return n

        # Solution 3: using regular expression, slow

        # find all codes by regular expression
        # import re

        # pattern = r'(\d\d#|\d)'
        # codes = re.findall(pattern, s)
        # print(codes)

        # res = ""
        # for each in codes:
        #     res = res + chr(int(each[:2]) + 96)
        # return res

        # Solution 4: using dictionary, faster

        # from collections import defaultdict
        # import string

        # dic = defaultdict(str)

        # for i, v in enumerate(string.ascii_lowercase):
        #     dic[str(i + 1)] = v

        # i = len(s) - 1
        # res = ''

        # while i >= 0:
        #     if s[i] == "#":
        #         res = dic[s[i - 2:i]] + res
        #         i = i - 3

        #     else:
        #         res = dic[s[i]] + res
        #         i = i - 1

        # return res


sol = Solution()
s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
print(sol.freqAlphabets(s))

"""
converting ascii to character and character to ascii:
https://en.wikibooks.org/wiki/Python_Programming/Text
"""
