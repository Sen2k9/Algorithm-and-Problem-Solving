"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""


class Solution:
    def strStr(self, haystack, needle):
        # Solution 1:

        # ned_size = len(needle)
        # hay_size = len(haystack)

        # if ned_size == 0 or haystack == needle:
        #     return 0
        # if ned_size > hay_size:
        #     return -1

        # for i in range(hay_size - ned_size + 1):
        #     if haystack[i: i + ned_size] == needle:
        #         return i
        # return - 1

        # Solution 2: using built-in function
        # if needle in haystack:
        #     return haystack.index(needle)
        # return - 1

        # Solution 3: using for-else, faster

        # if not needle or needle == haystack:
        #     return 0
        # if len(needle) > len(haystack):
        #     return -1

        # for i in range(len(haystack) - len(needle) + 1):
        #     for j in range(len(needle)):
        #         if needle[j] != haystack[i + j]:
        #             break
        #     else:
        #         return i

        # return - 1

        # Solution 4: using try-except block, clean code, O(1) memory

        # if needle == "":
        #     return 0

        # for i in range(len(haystack)):

        #     try:
        #         if haystack[i: i + len(needle)] == needle:
        #             return i
        #     except:
        #         break
        # return -1

        # Solution 5: more efficient

        if not needle:
            return 0
        if not haystack or len(haystack) < len(needle):
            return - 1

        ph = pn = l = 0
        h = len(haystack)
        n = len(needle)

        while ph < h - n + 1:

            while ph < h - n + 1 and haystack[ph] != needle[pn]:
                ph += 1

            while ph < h and pn < n and haystack[ph] == needle[pn]:
                #print(ph, pn)

                ph += 1
                pn += 1
                l += 1

            if l == n:
                return ph - l

            ph = ph - l + 1
            pn = l = 0

        return -1


sol = Solution()
haystack = "m"
needle = "m"
print(sol.strStr(haystack, needle))

"""
corner case:
1. needle string greater than haystack
"aaa"
"aaaa"

"mississippi"
"issip"
"mississippi"
"pi"


"""
