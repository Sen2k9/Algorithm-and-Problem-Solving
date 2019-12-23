"""
 Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
"""


class Solution:
    def isSubsequence(self, s, t):
        # Solution 1:
        # if len(s) > len(t):
        #     return False
        # if len(s) == 0:
        #     return True
        # seq = list(s)
        # seen = 0
        # for _, val in enumerate(t):
        #     if val == seq[0]:
        #         seq.remove(val)
        #         seen += 1
        #     if len(seq) == 0:
        #         return True
        #     print(seq)
        # return False

        # Solution 2: Optimized (12ms)
        index = -1
        # using enumerate instead of range saves memory space as well as runtime if you don't need to iterate the whole list, as enumerate used as iterator
        for _, val in enumerate(s):
            index = t.find(val, index+1)
            # find operation takes care all the corner case, including duplicate, ordering
            print(index)
            if index == -1:
                # this condition takes care of immediate execution if the sequence fails
                return False
        return True


sol = Solution()

s = "abx"
t = "ahbgdc"

print(sol.isSubsequence(s, t))
"""
Naive algorithm:
1. Store seen character
2. Check duplicate
3. Return true if all seen else false

Corner case:
1. len(s) > len(t)
2. s and/or t is empty
3. order of character between s and t are different: 
s = "agh"
t = "ahbgdc"
using only lookup for character fails for this test case. Always check the head for the lookup
4. empty("") subsequence is always a subsequence of given string
"""

"""
            The find() method returns the lowest index of the substring if it is found in given string. If its is not found then it returns -1.
            Syntax :

            str.find(sub,start,end)
            Parameters :

            sub : It’s the substring which needs to be searched in the given string.
            start : Starting position where sub is needs to be checked within the string.
            end : Ending position where suffix is needs to be checked within the string. 

            NOTE : If start and end indexes are not provided then by default it takes 0 and length-1 as starting and ending indexes where ending indxes is not included in our search. 
            https://www.geeksforgeeks.org/string-find-python/
"""
