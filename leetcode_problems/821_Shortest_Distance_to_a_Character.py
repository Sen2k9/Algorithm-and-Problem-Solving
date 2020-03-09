"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

Note:

    S string length is in [1, 10000].
    C is a single character, and guaranteed to be in string S.
    All letters in S and C are lowercase.
"""


class Solution:
    def shortestToChar(self, S: str, C: str):
        result = []
        loc = S.find(C)
        for i in range(len(S)):
            found = False

            if S[i] == C:
                result.append(0)
                loc = i
                continue
            for j in range(i + 1, len(S)):
                if S[j] == C:
                    if abs(loc - i) < abs(i - j):
                        result.append(abs(loc - i))
                    else:

                        result.append(abs(i - j))
                    found = True
                    break
            if found == False:
                result.append(abs(loc - i))
        return result


sol = Solution()

S = "loveleetcode"
C = 'e'
print(sol.shortestToChar(S, C))
