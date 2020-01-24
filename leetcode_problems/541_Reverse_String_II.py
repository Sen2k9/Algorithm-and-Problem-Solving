"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string.
If there are less than k characters left, reverse all of them.
If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

Example:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Restrictions:

    The string consists of lower English letters only.
    Length of the given string and k will in the range [1, 10000]
"""


class Solution:
    def reverseStr(self, s: str, k: int):
        # Solution 1: self
        # res = ""
        # start = 0
        # n = len(s)
        # while 2 * k <= n:
        #     res = res + s[start: start + k][::-1] + \
        #         s[start + k: 2 * k + start]
        #     start = start + 2*k

        #     n = n - (2 * k)
        # print(n, start)
        # if n < k:
        #     res = res + s[start:][::-1]
        # elif n < 2 * k and n >= k:
        #     res = res + s[start: start + k][::-1] + s[start + k:]
        # return res

        # Solution 2: sliding window, faster

        # res = ""
        # i = 0
        # j = 2 * k
        # while i < len(s):
        #     if j <= len(s):
        #         res = res + s[i:i+k][::-1] + s[i+k:j]
        #         i = j
        #         j = j + (2 * k)

        #     elif j > len(s) and i <= len(s):
        #         res = res + s[i: i + k][::-1] + s[i + k:]
        #         break

        #     elif len(s) < i:
        #         res = res + s[i:][::-1]
        #         break
        # return res

        # Solution 3: recursive

        # if len(s) < k:
        #     return s[::-1]

        # elif len(s) < (2 * k) and len(s) >= k:
        #     return s[:k][::-1] + s[k:]

        # else:
        #     return s[:k][::-1] + s[k: 2 * k] + self.reverseStr(s[2 * k :], k)

        # Solution 4: easy, fastest

        n = len(s)
        if n < k:
            return s[::-1]
        if n >= k and n < 2 * k:
            return s[:k][::-1]+s[k:]
        res = ""
        for i in range(0, n, 2 * k):
            res = res + s[i: i + k][::-1] + s[i + k: i + (2 * k)]

        return res


sol = Solution()
s = "abcdefghijklmnop"
k = 3
print(sol.reverseStr(s, k))
