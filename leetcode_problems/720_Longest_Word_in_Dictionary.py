"""
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.
If there is no answer, return the empty string.

Example 1:

Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:

Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

Note:
All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
"""


class Solution:
    def longestWord(self, words):
        # Solution 1: easy & readable
        # O(n)
        words = sorted(words)

        word_set = set()
        result = ""

        word_set.add("")

        for each in words:
            if each[:-1] in word_set:
                word_set.add(each)

                if len(each) > len(result):
                    result = each
        # print(word_set)
        return result


sol = Solution()
words = ["a", "b", "ba", "ban", "bann", "banna", "bannan",
         "bannana", "app", "appl", "ap", "apply", "apple"]
print(sol.longestWord(words))

"""
corner case:
1. longest valid word is in last element
2. multiple valid words
3. multiple valid same length words
4. for the longest valid word, their must have to be a single word which represent the first character of the longest valid word.
for example: "a" for "apple", "b" for "bannana"
["a", "b", "ba", "ban", "bann", "banna", "bannan",
         "bannana", "app", "appl", "ap", "apply", "apple"]

reference:
https://leetcode.com/problems/longest-word-in-dictionary/discuss/367203/easy-peasy-python-solution-using-sorting-and-set
"""
