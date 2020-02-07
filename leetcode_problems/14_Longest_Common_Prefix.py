"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.
"""


class Solution:
    def longestCommonPrefix(self, strs):
        # solution 1: self
        # if not strs:
        #     return ""
        # f = strs[0]

        # for i in range(len(f)):
        #     for j in range(1, len(strs)):
        #         if i < len(strs[j]) and f[i] == strs[j][i]:
        #             continue
        #         else:
        #             return "".join(list(f)[:i])
        # return f

        # solution 2: faster
        t = 0

        for i in zip(*strs):
            if len(set(i)) == 1:
                t += 1
            else:
                break
        # print(t)
        return strs[0][:t] if strs else ""


sol = Solution()
s = ["dog", "racecar", "car"]
print(sol.longestCommonPrefix(s))
assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
