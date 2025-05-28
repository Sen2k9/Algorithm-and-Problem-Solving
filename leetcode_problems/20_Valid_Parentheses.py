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
import unittest

class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for char in s:

            if stack and stack[-1] == match.get(char, ""):
                stack.pop()
            
            else:
                stack.append(char)
        
        return True if not stack else False


class TestSuite(unittest.TestCase):
    
    def test_valid_parentheses(self):
        sol = Solution()
        
        input = "()"
        
        self.assertEqual(
            sol.isValid(input),
            True
        )
        
        input = "(]"
        
        self.assertEqual(
            sol.isValid(input),
            False
        )

if __name__ == "__main__":
    unittest.main()