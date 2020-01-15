"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 20
    order.length == 26
    All characters in words[i] and order are English lowercase letters.

"""


class Solution:
    def isAlienSorted(self, words, order):
        # Solution 1: self

        # def checkIndex(ch, order):
        #     return order.index(ch)

        # if len(words) == 1:
        #     for j in range(len(words[0]) - 1):
        #         if checkIndex(words[0][j], order) > checkIndex(words[0][j + 1], order):
        #             return False
        #     else:
        #         return True

        # for i in range(len(words) - 1):
        #     j = 0

        #     while j < min(len(words[i]), len(words[i + 1])):

        #         if checkIndex(words[i][j], order) > checkIndex(words[i + 1][j], order):
        #             return False
        #         elif checkIndex(words[i][j], order) == checkIndex(words[i + 1][j], order):
        #             j += 1
        #             continue
        #         # covers corner case 3
        #         elif checkIndex(words[i][j], order) < checkIndex(words[i + 1][j], order):
        #             break

        #     # To cover corner case 2 and 4

        #     if j == min(len(words[i]), len(words[i + 1])) and not checkIndex(words[i][j-1], order) < checkIndex(words[i + 1][j-1], order) and len(words[i]) > len(words[i + 1]):

        #         return False

        # return True

        # Solution 2: using dictionary, slow

        # dic = {}

        # for i in range(len(order)):
        #     dic[order[i]] = i

        # while len(words) > 1:

        #     for i in range(len(words[0])):
        #         if dic[words[0][i]] < dic[words[1][i]]:
        #             words = words[1:]
        #             break
        #         if dic[words[0][i]] > dic[words[1][i]]:
        #             return False

        #         if i == len(words[0]) - 1:
        #             words = words[1:]

        #         if i == len(words[1]) - 1:  # covers corner case 4
        #             return False

        # return True

        # Solution 3: using list comprehension

        words_value = [[order.index(ch) for ch in word] for word in words]

        while len(words_value) > 1:

            for i in range(len(words_value[0])):
                if words_value[0][i] < words_value[1][i]:
                    words_value = words_value[1:]
                    break

                elif words_value[0][i] > words_value[1][i]:
                    return False

                elif i == len(words_value[0]) - 1:
                    words_value = words_value[1:]

                elif i == len(words_value[1]) - 1:
                    return False

        return True


sol = Solution()
words = ["kuvp", "q"]
order = "ngxlkthsjuoqcpavbfdermiywz"
print(sol.isAlienSorted(words, order))

"""
corner cases:
1. one words only

2. ["kuvp","q"]
"ngxlkthsjuoqcpavbfdermiywz"

3. words = ["fxasxpc", "dfbdrifhp", "nwzgs", "cmwqriv", "ebulyfyve",
         "miracx", "sxckdwzv", "dtijzluhts", "wwbmnge", "qmjwymmyox"]
order = "zkgwaverfimqxbnctdplsjyohu"

4. words = ["apple", "app"]
order = "abcdefghijklmnopqrstuvwxyz"
"""
