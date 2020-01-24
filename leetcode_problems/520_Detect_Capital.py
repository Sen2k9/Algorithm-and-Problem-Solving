"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:

Input: "USA"
Output: True

Example 2:

Input: "FlaG"
Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""


class Solution:
    def detectCapitalUse(self, word: str):
        # Solution 1:self
        # if word == word.upper():
        #     return True
        # elif word == word.lower():
        #     return True
        # elif word == word[0] + word[1:].lower():
        #     return True
        # else:
        #     return False

        # Solution 2:self, faster
        if word[0].islower():
            for each in word[1:]:
                if not each.islower():
                    return False
        elif word[0].isupper():
            for i in range(1, len(word) - 1):
                print(word[i], word[i+1])
                if word[i].isupper() != word[i + 1].isupper():
                    return False

        return True
        # Solution 3: slower
        # print(word.title())
        return word in [word.upper(), word.lower(), word.title()]
        # reference: https://leetcode.com/problems/detect-capital/discuss/336441/Solution-in-Python-3-(one-line)


sol = Solution()
word = "GSA"
print(sol.detectCapitalUse(word))
