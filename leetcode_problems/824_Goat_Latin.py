"""
A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

    If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
    For example, the word 'apple' becomes 'applema'.
     
    If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
    For example, the word "goat" becomes "oatgma".
     
    Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
    For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.

Return the final sentence representing the conversion from S to Goat Latin. 

Example 1:

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

Example 2:

Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

Notes:

    S contains only uppercase, lowercase and spaces. Exactly one space between each word.
    1 <= S.length <= 150.

"""


class Solution:
    def toGoatLatin(self, S: str):
        # Solution 1: self, 96%
        l = S.split()
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        output = []
        for i, each in enumerate(l, start=1):
            if each[0] in vowels:
                each = each + "ma"
            else:
                each = each[1:] + each[0] + "ma"
            each = each + ("a" * i)
            output.append(each)
        return " ".join(output)

        # Solution 2: not using join
        # s = ''
        # i = 1
        # vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        # for word in S.split(' '):
        #     if word[0] in vowels:
        #         s += word + 'ma' + 'a'*i
        #     else:
        #         s += word[1:] + word[0] + 'ma' + 'a'*i
        #     i += 1
        #     s += ' '

        # return s[:-1]


sol = Solution()
S = "The quick brown fox jumped over the lazy dog"
print(sol.toGoatLatin(S))
"""
corner case:
words consist of upper and lower case letters
"""
