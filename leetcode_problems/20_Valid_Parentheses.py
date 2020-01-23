"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true
"""


class Solution:
    def isValid(self, s: str):
        # Solution 1: self
        stack = []
        # stack.append(s[0])

        for each in s:
            if not stack:
                stack.append(each)
            elif stack[-1] == "(" and each == ")":
                stack.pop()
            elif stack[-1] == "{" and each == "}":
                stack.pop()
            elif stack[-1] == "[" and each == "]":
                stack.pop()
            else:
                stack.append(each)

        return len(stack) == 0
        # Solution 2:
        stack = []

        for each in s:
            if each in ["(", "{", "["]:
                stack.append(each)
            elif len(stack) == 0:
                return False

            elif each == ")" and stack.pop() != "(":
                return False
            elif each == "}" and stack.pop() != "{":
                return False
            elif each == "]" and stack.pop() != "[":
                return False
        return len(stack) == 0


sol = Solution()
s = ""
print(sol.isValid(s))
"""
corner case:
1. should check stack first and the coming string
"]"
"""
