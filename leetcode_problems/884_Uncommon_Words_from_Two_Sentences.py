"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]

Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]

Note:

    0 <= A.length <= 200
    0 <= B.length <= 200
    A and B both contain only spaces and lowercase letters.

"""


class Solution:
    def uncommonFromSentences(self, A, B):
        # Solution 1: self
        # if not len(A) and not len(B):
        #     return []
        # elif not len(A):
        #     return B.split()
        # elif not len(B):
        #     return A.split()
        # dic = {}
        # res = []
        # s = A + " "+B
        # for each in s.split():
        #     dic[each] = dic.get(each, 0) + 1
        # for k, v in dic.items():
        #     if v == 1:
        #         res.append(k)
        # return res

        # Solution 2:

        import collections

        c = collections.Counter((A + " " + B).split())
        print(c)
        return [w for w in c if c[w]==1]




sol = Solution()
A = "apple apple"
B = "banana"
print(sol.uncommonFromSentences(A,B))
