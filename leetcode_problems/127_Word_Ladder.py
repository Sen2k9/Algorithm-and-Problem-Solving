"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list.

Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0

        all_combo_dictionary = defaultdict(list)

        L = len(beginWord) # all words are same length

        # time and space O(L*N)
        for word in wordList:
            for index in range(L):
                all_combo_dictionary[word[:index] + "*" + word[index+1:]].append(word)

        print(all_combo_dictionary)

        queue = deque()
        queue.append((beginWord, 1))
        visited = defaultdict(bool)
        visited[beginWord] = True

        # O(N)
        while queue:
            node, level = queue.popleft()

            # O(L*N)
            for i in range(L):
                intermediate_word = node[:i] + "*" + node[i+1:]

                for word in all_combo_dictionary[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    
                    if visited[word]:
                        continue
                    
                    visited[word] = True
                    queue.append((word, level + 1))
            
            print(queue)

        return 0



sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(sol.ladderLength(beginWord, endWord, wordList))

beginWord = "hot"
endWord = "dog"
wordList = ["hot", "dog"]

print(sol.ladderLength(beginWord, endWord, wordList))