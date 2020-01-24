"""
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.
Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

Note:

    1 <= str1.length <= 1000
    1 <= str2.length <= 1000
    str1[i] and str2[i] are English uppercase letters.
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str):
        # Solution 1:

        print(str1, str2)

        if str1 == str2:
            return str2

        else:
            if len(str1) > len(str2) and str2 in str1:
                return self.gcdOfStrings(str2, str1[len(str2):])
            elif len(str2) > len(str1) and str1 in str2:
                return self.gcdOfStrings(str1, str2[len(str1):])
        return ""


sol = Solution()
s1 = "ABCDEF"
s2 = "ABC"
print(sol.gcdOfStrings(s1, s2))
"""
corner case:
str1 = "ABC"
str2 = "ABCDEF"
"TAUXXTAUXXTAUXXTAUXXTAUXX"
"TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"

https://leetcode.com/problems/greatest-common-divisor-of-strings/discuss/484713/Python-O(-log-n-)-sol.-based-on-gcd.-90%2B-With-explanation

https://leetcode.com/problems/greatest-common-divisor-of-strings/discuss/426882/python-understandable-from-numerical-gcd
"""
