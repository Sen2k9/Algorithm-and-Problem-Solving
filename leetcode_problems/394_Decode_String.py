"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

"""


class Solution:
    def decodeString(self, s: str):
        if not s:
            return ""

        stack = []

        for i in s:
            if i.isdigit() or i.isalpha() or i == "[":
                stack.append(i)

            elif i == "]":
                temp = ""

                while stack[-1] != "[":
                    temp = stack.pop() + temp

                time = ""
                stack.pop()

                # this loop is for numbers which may have more than one digits
                while stack and stack[-1].isdigit():
                    time = stack.pop() + time

                stack.append(temp * int(time))

            print(stack)

        return "".join(stack)


sol = Solution()
s = "100[leetcode]"
print(sol.decodeString(s))

"""
references:
https://leetcode.com/problems/decode-string/discuss/459263/Easy-to-understand-Python-Stack-solution
"""
