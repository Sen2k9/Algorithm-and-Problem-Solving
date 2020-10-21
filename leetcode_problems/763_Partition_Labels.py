"""
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

    S will have length in range [1, 500].
    S will consist of lowercase English letters ('a' to 'z') only.
"""
from collections import defaultdict


class Solution:
    def partitionLabels(self, S: str):
        char_dic = defaultdict(int)
        for i, char in enumerate(S):
            char_dic[char] = i  # last occurance of char in the string
            
        ans = []
        # print(char_dic)
        i = 0
        offset = 0
        
        for j, char in enumerate(S):
            i = max(i, char_dic[char])
            
            if i == j:
                #print(offset, j)
                ans.append(j - offset + 1)
                offset = j + 1
                #print(offset)

        return ans


sol = Solution()
S = "ababcbacadefegdehijhklij"
print(sol.partitionLabels(S))
