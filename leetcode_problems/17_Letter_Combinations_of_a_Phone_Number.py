"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""


class Solution:
    def letterCombinations(self, digits: str):
        dictionary = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(combination, new_digits):
            if len(new_digits) == 0:
                ans.append(combination)

            else:
                for each in dictionary[new_digits[0]]:
                    backtrack(combination + each, new_digits[1:])

        ans = []
        backtrack("", digits)
        return ans


sol = Solution()
digits = "23"
print(sol.letterCombinations(digits))
