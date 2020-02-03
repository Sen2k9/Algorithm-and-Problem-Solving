"""
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.
Example:

Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.

Note:

    1 <= paragraph.length <= 1000.
    0 <= banned.length <= 100.
    1 <= banned[i].length <= 10.
    The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
    paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
    There are no hyphens or hyphenated words.
    Words only consist of letters, never apostrophes or other punctuation symbols.
"""


class Solution:
    def mostCommonWord(self, paragraph, banned):
        # Solution 1: self
        # Runtime: O(n!), python use backtracking for regx (https://towardsdatascience.com/regex-performance-in-python-873bd948a0ea)
        # Memory: O(n)

        import re
        from collections import Counter
        # regx is easy to use but has high runtime
        # lots of way to be efficient in regex
        l = re.findall(r'\w+', paragraph)
        print(l)
        dic = {}
        for each in l:
            if each.lower() in dic:
                dic[each.lower()] += 1
            else:
                dic[each.lower()] = 1
        print(dic)
        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        print(dic)
        for k, _ in dic:  # can not use items() because sorted function in python convert dictionary to list of tuples
            if k not in banned:
                return k

        # Solution 2: faster
        # Runtime: O(nlogn)
        # Memory : O(n)
        l = paragraph.split()
        punc = ["?", "!", "'", ",", ";", "."]
        dic = {}
        for each in l:  # this loop has O(5n) ~ O(n) complexity
            s = []
            for i in punc:
                if i in each:

                    s = each.split(i)
                    break

            else:
                s = [each]
            # print(s[0])
            if s[0].lower() not in dic:
                dic[s[0].lower()] = 1
            else:
                dic[s[0].lower()] += 1

        # Assuming every words are unique, the sorting takes standard time O(nlogn)
        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

        for k, _ in dic:
            if k not in banned:
                return k

        # Solution 3: fastest
        # Runtime : O(n)
        # Memory : O(n)
        l = paragraph.split()
        punc = ["?", "!", "'", ",", ";", "."]
        dic = {}
        for each in l:  # this loop has O(5n) ~ O(n) complexity
            s = []
            for i in punc:
                if i in each:

                    s = each.split(i)
                    break

            else:
                s = [each]
            # print(s[0])
            if s[0].lower() not in dic:
                dic[s[0].lower()] = 1
            else:
                dic[s[0].lower()] += 1
        ans = ["", -1]
        for k, v in dic.items():
            if k not in banned and v > ans[1]:
                ans = [k, v]
        return ans[0]


sol = Solution()
paragraph = "Bob hit? a ball, the hit BALL flew far after it was hit."
banned = []
print(sol.mostCommonWord(paragraph, banned))
"""
!?',;.
"""
