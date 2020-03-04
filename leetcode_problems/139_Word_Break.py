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


class Solution:
    def wordBreak(self, s, wordDict):
        temp = ""
        for i in range(len(wordDict)):
            temp = s
            sp = temp.split(wordDict[i])
            temp = temp.replace(wordDict[i], "")

            #s = "".join(s)
            print(temp, sp)
            if temp not in sp:
                return False

            sp = temp

            for j in range(len(wordDict)):
                if j == i:
                    continue
                sp = temp.split(wordDict[j])
                temp = temp.replace(wordDict[j], "")
                if temp not in sp:
                    break
                #print(temp, sp)
                sp = temp

                if not temp:

                    return True
            if not temp:
                return True
            #print(temp)
        return False


sol = Solution()
s = "ccaccc"
w = ["cc", "ac"]

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
