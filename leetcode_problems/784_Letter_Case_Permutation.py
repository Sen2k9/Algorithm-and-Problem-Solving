"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]

Note:

    S will be a string with length between 1 and 12.
    S will consist only of letters or digits.

"""


class Solution:
    def letterCasePermutation(self, S):
        def backtrack(sub="", i=0):
            if len(sub) == len(S):
                res.append(sub)
            else:
                if S[i].isalpha():
                    backtrack(sub + S[i].swapcase(), i + 1)
                backtrack(sub+S[i], i+1)

        res = []
        backtrack()

        return res


sol = Solution()
S = "mQe"
print(sol.letterCasePermutation(S))
"""
Algo:
Starting from an empty string, we incrementally go through the entire string S.

In each backtracking step, we check whether that character is alphabetic or not.
If True, there are two cases should be considered: (1) upper case and (2) lower case.
If False, only one backtracking case.

The program stops until we go through the entire string, step == len(S).

Please let me know if there is somewhere can be improved.

reference:
https://leetcode.com/problems/letter-case-permutation/discuss/379928/Python-clear-solution
"""
