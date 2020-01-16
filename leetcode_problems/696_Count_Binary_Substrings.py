"""
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:

Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:

Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

Note:
s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
"""


class Solution:
    def countBinarySubstrings(self, s: str):
        # Solution 1:

        # stack = [[], []]

        # prev = int(s[0])
        # res = 0

        # for i in range(1, len(s)):
        #     curr = int(s[i])
        #     if curr != prev:
        #         stack[curr].clear()
        #         prev = curr
        #     stack[curr].append(curr)
        #     if len(stack[1 - curr]) > 0:
        #         stack[1 - curr].pop()
        #         res += 1

        # return res

        # Solution 2: fastest
        # https://leetcode.com/problems/count-binary-substrings/discuss/108625/PythonC%2B%2BJava-Easy-and-Concise-with-Explanation

        # take a string for eg 00101110011
        # then we split the 01 to 0 1 and 10 to 1 0, so essentially we include a space when a zero bit changes to one and vice versa
        # so the result will be 00 1 0 111 00 11
        # then you simply do a split and a len on the sting

        s = s.replace("01", "0 1")
        s = s.replace("10", "1 0")
        # print(s)

        l = list(map(len, s.split()))
        res = 0
        for a, b in zip(l, l[1:]):
            res += min(a, b)

        return res


sol = Solution()
s = "00110011"
print(sol.countBinarySubstrings(s))
