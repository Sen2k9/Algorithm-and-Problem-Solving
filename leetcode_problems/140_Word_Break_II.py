"""
    Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

 

Constraints:

    1 <= s.length <= 20
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 10
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.
    Input is generated in a way that the length of the answer doesn't exceed 105.


"""
from typing import List
import unittest

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dictionary = {word for word in wordDict}
        answer = []

        def backtrack(idx, temp):
            if idx >= len(s):
                answer.append(
                    " ".join(temp)
                )
                return
            
            for j in range(idx, len(s) + 1):
                if s[idx: j] in dictionary:
                    temp.append(s[idx : j]) # add

                    # find words starting from j
                    backtrack(j, temp) # do dfs
                    #print(temp)
                    temp.pop() # remove
        
        backtrack(0, [])

        return answer

class TestSuite(unittest.TestCase):
    
    def test_wordBreak(self):
        # call the solution class
        sol = Solution()
        
        # test the method of that solution
        s = "catsanddog"; wordDict = ["cat","cats","and","sand","dog"]
        answer = ["cat sand dog", "cats and dog"]
        self.assertEqual(
            sol.wordBreak(s, wordDict),
            answer,
            "Passed Gracefully"
        )
        
        s = "catsandog"; wordDict = ["cats","dog","sand","and","cat"]
        answer = []
        self.assertEqual(
            sol.wordBreak(s, wordDict),
            answer,
            "Passed Gracefully"
        )

if __name__ == "__main__":
    unittest.main()