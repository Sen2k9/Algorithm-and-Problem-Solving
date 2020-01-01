"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:

    1 <= S.length <= 200
    1 <= T.length <= 200
    S and T only contain lowercase letters and '#' characters.

Follow up:

    Can you solve it in O(N) time and O(1) space?

"""


class Solution:
    def backspaceCompare(self, S: str, T: str):
        # Solution 1: self
        # O(N)
        # remove = 0

        # s = ""
        # for i in range(len(S)-1, -1, -1):
        #     if S[i] == "#":
        #         remove += 1
        #     elif remove > 0:
        #         remove -= 1
        #     else:
        #         s += S[i]
        # remove = 0
        # t = ""
        # for i in range(len(T) - 1, -1, -1):
        #     if T[i] == "#":
        #         remove += 1
        #     elif remove > 0:
        #         remove -= 1
        #     else:
        #         t += T[i]
        # print(s, t)
        # return s == t

        # Solution 2: two pointer
        ans = ''
        ans_2 = ''
        for i in S:
            if i == '#':
                ans = ans[:-1]
            else:
                ans += i
            # print(ans)

        for i in T:
            if i == '#':
                ans_2 = ans_2[:-1]
            else:
                ans_2 += i
            # print(ans)
        return ans == ans_2


sol = Solution()
S = "ab#c"
T = "ad#c"
print(sol.backspaceCompare(S, T))
