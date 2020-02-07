"""
 Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:

Input: "aba"
Output: True

Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:

    The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""


class Solution:
    def validPalindrome(self, s: str):
        i = 0
        j = len(s) - 1
        even = len(s) % 2 == 0
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            else:

                A = s[:i] + s[i + 1:]
                B = s[:j] + s[j + 1:]
                mid = len(A)//2

                if even:
                    return A[:mid] == A[mid + 1:][::-1] or B[:mid] == B[mid + 1:][::-1]
                else:
                    return A[:mid] == A[mid:][::-1] or B[:mid] == B[mid:][::-1]
        return True


sol = Solution()
s = "abgcddchba"
print(sol.validPalindrome(s))
