"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Example 1:

Input: "A"
Output: 1

Example 2:

Input: "AB"
Output: 28

Example 3:

Input: "ZY"
Output: 701
"""


class Solution:
    def titleToNumber(self, s: str):
        # Solution 1: self
        # O(n), where n is the length of the string
        # O(1), we only need one variable result to store the answer
        if not s.isalpha():
            return 0
        s = s.upper()
        result = 0
        for i in range(len(s)):
            result = result + 26 ** (i) * (ord(s[len(s) - 1 - i]) - 64)
        return result


sol = Solution()
s = "ABC"
print(sol.titleToNumber(s))
"""
corner case:
1. no valid letters
2. small or special characters
"""
