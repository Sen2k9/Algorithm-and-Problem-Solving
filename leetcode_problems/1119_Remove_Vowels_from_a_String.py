"""
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

 

Example 1:

Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"

Example 2:

Input: "aeiou"
Output: ""

 

Note:

    S consists of lowercase English letters only.
    1 <= S.length <= 1000

"""


class Solution:
    def removeVowels(self, S: str):
        # Solution 1: using join
        # return "".join([i for i in list(S) if i not in ['a', 'e', 'i', 'o', 'u']])

        # Solution 2: using filter
        return "".join(filter(lambda x: x not in set("aeiou"), list(S)))


sol = Solution()
S = "leetcodeisacommunityforcoders"
print(sol.removeVowels(S))
assert sol.removeVowels("") == ""
