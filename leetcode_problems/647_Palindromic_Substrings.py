"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:

    The input string length won't exceed 1000.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        # result = 0

        # for index in range(2*len(s) - 1):
        #     left = index // 2
        #     right = left + (index % 2)

        #     while left >= 0 and right < len(s) and s[left] == s[right]:
        #         result += 1
        #         left -= 1
        #         right += 1

        # return result

        # Dynamic Programming

        matrix = [[0 for _ in range(len(s))] for _ in range(len(s))]
        #print(matrix)
        result = 0

        for i in range(len(s)):
            matrix[i][i] = 1
            result += 1

        for col in range(1, len(s)):
            for row in range(col):

                # check for two element

                if row == col -1 and s[row] == s[col]:
                    matrix[row][col] = 1
                    result += 1

                elif matrix[row + 1][col - 1] == 1 and s[row] == s[col]:
                    matrix[row][col] = 1
                    result += 1

        print(matrix)
        return result


sol = Solution()
s = "aaa"
print(sol.countSubstrings(s))

s = "abc"
print(sol.countSubstrings(s))

s = "racecar"
print(sol.countSubstrings(s))