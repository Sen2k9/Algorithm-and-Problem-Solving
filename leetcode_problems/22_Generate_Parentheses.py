"""
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def generateParenthesis(self, n: int):
        result = []

        self.helper(n, n, "", result)
        return result

    def helper(self, openBraket, closingBraket, path, result):
        if openBraket == 0 and closingBraket == 0:
            result.append(path)

        else:
            if closingBraket > 0 and openBraket < closingBraket:
                self.helper(openBraket, closingBraket - 1, path + ")", result)
            if openBraket > 0:
                self.helper(openBraket - 1, closingBraket, path + "(", result)


sol = Solution()
n = 5
print(sol.generateParenthesis(n))
