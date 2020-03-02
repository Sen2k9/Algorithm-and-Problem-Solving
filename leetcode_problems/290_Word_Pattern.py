"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

"""


class Solution:
    def wordPattern(self, pattern: str, str: str):
        # Solution: self
        # Time O(n)
        # Space O(n)

        dic = {}

        pattern_set = set()
        word_set = set()
        str = str.split()
        if len(pattern) != len(str):  # test case : "aaa", "ab ab ab ab"
            return False
        # print(str)

        for i in range(len(pattern)):
            # print(pattern[i])
            if pattern[i] in dic:  # test case : "aabb" "dog cat cat dog"
                #print(dic[pattern[i]], str[i])
                if dic[pattern[i]] != str[i]:
                    return False
            # print(dic)
            dic[pattern[i]] = str[i]
            pattern_set.add(pattern[i])
            word_set.add(str[i])

            # print(dic)
        if len(pattern_set) != len(word_set):  # test case : "abba" "dog dog dog dog"

            return False
        return True


sol = Solution()
pattern = "abc"
s = "b c a"


print(sol.wordPattern(pattern, s))
