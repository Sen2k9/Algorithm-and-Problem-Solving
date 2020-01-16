"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Example 1:

Input: "ab-cd"
Output: "dc-ba"

Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Note:

    S.length <= 100
    33 <= S[i].ASCIIcode <= 122 
    S doesn't contain \ or "

"""


class Solution:
    def reverseOnlyLetters(self, S: str):
        # Solution 1: self
        import re
        # print(len(S))

        s = S
        # everything matches non-word character [^A-Za-z] replaced by empty string("")
        s = re.sub(r'[^A-Za-z]', "", s)  # it covers corner case 1 and 2 also
        # print(s)
        i = len(s) - 1
        j = 0
        res = ''

        # if there is no letter in origin string i will be 0 but j will iterate for the special characters
        while j < len(S) and i >= -1:
            # which covers corner case 1,2
            if not S[j].isalpha():
                res = res + S[j]
                j += 1

            else:
                res = res + s[i]
                i -= 1  # after exhausting all letters this one will give -1
                j += 1
            #print(i, j)
        return res

        # Soluion 2: using list and join

        # l = list(S)

        # i = 0
        # j = len(l) - 1

        # while i <= j:
        #     if S[i].isalpha() and S[j].isalpha():
        #         temp = l[j]
        #         l[j] = l[i]
        #         l[i] = temp
        #         i += 1
        #         j -= 1

        #     elif not S[i].isalpha():
        #         i += 1
        #     else:
        #         j -= 1

        # return "".join(l)

        # Solution 3: separating alpha and non-alpha
        # non_alpha = [(i, S[i])
        #              for i in range(len(S)) if not S[i].isalpha()]

        # reverse = [char for char in S if char.isalpha()][::-1]

        # print(non_alpha, reverse)

        # for each in non_alpha:
        #     reverse.insert(each[0], each[1])

        # return "".join(reverse)
        # https://leetcode.com/problems/reverse-only-letters/discuss/329204/4-lines-fast-and-efficient-Python-with-commentary

        # Solution 4: slow

        # c = [char for char in S if char.isalpha()]
        # S = list(S)

        # for i in range(len(S) - 1, -1, -1):
        #     if S[i].isalpha():
        #         S[i] = c.pop(0)
        # return "".join(S)
        # https://leetcode.com/problems/reverse-only-letters/discuss/337853/Solution-in-Python-3


sol = Solution()
S = "-S2_"
print(sol.reverseOnlyLetters(S))
"""
corner case:
1. empty string
2. no letter


"""
