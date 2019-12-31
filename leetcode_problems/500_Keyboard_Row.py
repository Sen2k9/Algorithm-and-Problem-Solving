"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:

    You may use one character in the keyboard more than once.
    You may assume the input string will only contain letters of alphabet.

"""


class Solution:
    def findWords(self, words):
        # solution 1: self
        # first = "qwertyuiop"
        # second = "asdfghjkl"
        # third = "zxcvbnm"
        # output = []

        # for each in words:
        #     valid = True
        #     l = list(each.lower())
        #     if l[0] in first:
        #         for c in l:
        #             if c not in first:
        #                 valid = False

        #                 break
        #         if valid:
        #             output.append(each)

        #     elif l[0] in second:
        #         for c in l:
        #             if c not in second:
        #                 valid = False
        #                 break
        #         if valid:
        #             output.append(each)

        #     elif l[0] in third:
        #         for c in l:
        #             if c not in third:
        #                 valid = False
        #                 break
        #         if valid:
        #             output.append(each)
        # return output

        # Solution 2: using subset, pythonic and efficient
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")
        output = []
        for each in words:
            l = set(each.lower())  # ignorecase

            if l.issubset(first) or l.issubset(second) or l.issubset(third):
                output.append(each)
        return output


sol = Solution()
words = ["Hello", "Alaska", "Dad", "Peace"]
print(sol.findWords(words))
"""
to use ignorecase in python make all strings to lowercase

Subset in Python:
https://www.programiz.com/python-programming/methods/set/issubset
"""
