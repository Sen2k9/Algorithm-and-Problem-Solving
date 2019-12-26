"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space and there will not be any extra space in the string.

"""


class Solution:
    def reverseWords(self, s):
        # Solution 1: self
        # if len(s) < 2:
        #     return s
        # result = ""
        # temp = ""
        # for each in s:

        #     if each == " ":
        #         result = result + temp + each
        #         temp = ""

        #     else:
        #         temp = each + temp
        #     #print(result, temp)
        # if len(temp):
        #     result = result + temp
        # return result

        # Solution 2: faster, pythonic way: split, reverse, join
        # words = s.split(" ")
        # result = []
        # for word in words:
        #     result.append(word[::-1])
        # # print(result)
        # return " ".join(result)

        # Solution 3: fastest and memory efficient
        if len(s) < 2:
            return s

        words = s.split(" ")
        for i in range(len(words)):
            words[i] = words[i][::-1]

        return " ".join(words)


sol = Solution()
s = " Let's take LeetCode contest"
print(sol.reverseWords(s))

"""
corner case:
1. empty string
2. start and/or end with whitespace
"""
