"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.

Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

"""
from collections import deque

class Solution:
    def wordBreak(self, s, wordDict):
        # BFS algorithm
        word_set = set(wordDict)
        visited = [0] * len(s)
        queue = deque()
        queue.append(0)
        while queue:
            start = queue.popleft()
            if visited[start] == 0:
                for end in range(start + 1, len(s)+1):
                    if s[start:end] in word_set:
                        queue.append(end)

                        if end == len(s):
                            return True

                visited[start] = 1

            print(queue)

        return False



sol = Solution()
s = "cbca"
w = ["bc","ca"]

print(sol.wordBreak(s, w))

"""
corner case:
"cars"
["car","ca","rs"]

"a"
["a"]

"cbca"
["bc","ca"]

"""
