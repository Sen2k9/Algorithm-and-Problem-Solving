"""
In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.

 

Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.

Example 2:

Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.

Example 3:

Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]

 

Note:  1 <= S.length <= 1000

"""


class Solution:
    def largeGroupPositions(self, S):
        group = []
        start = 0
        end = 0
        value = S[0]
        count = 1

        for i in range(1, len(S)):
            if count >= 3:
                if S[i] != value:
                    end = i - 1
                    group.append([start, end])
                    end = 0

            if S[i] == value:
                count += 1
            else:
                value = S[i]
                count = 1
                start = i
        #  Checks if there was a large group at the end of the string
        if count >= 3:
            group.append([start, len(S)-1])
        return group


sol = Solution()

S = "abbb"

print(sol.largeGroupPositions(S))

""""
corner case:
S = "aaa"
S = "abbb"
S = "abbbccc"

"""
