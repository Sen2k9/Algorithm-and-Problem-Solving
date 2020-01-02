"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.

You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2

Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1

Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3

 

Note:

    1 <= N <= 1000
    trust.length <= 10000
    trust[i] are all different
    trust[i][0] != trust[i][1]
    1 <= trust[i][0], trust[i][1] <= N


"""


class Solution:
    def findJudge(self, N, trust):
        # Solution 1: self
        # if not trust:
        #     return N
        # indegre = {}
        # out = {}
        # result = -1
        # for each in trust:
        #     out[each[0]] = out.get(each[0], 0) + 1
        #     indegre[each[1]] = indegre.get(each[1], 0) + 1
        #     #print(indegre, out)
        #     if indegre[each[1]] == N - 1:
        #         result = each[1]
        #     if out.get(result, 0) != 0:
        #         result = -1

        # return result

        # Solution 2: using adjacency matrix

        outdegree = {}
        indegree = []

        for _ in range(N + 1):
            indegree.append([])

        for a, b in trust:
            outdegree[a] = 1
            indegree[b].append(a)

        for i in range(1, N + 1):
            if len(indegree[i]) == N - 1 and i not in outdegree:
                return i
        return -1


sol = Solution()
N = 3
trust = [[1, 3], [2, 3], [3, 1]]
print(sol.findJudge(N, trust))
"""
corner case:
1. judge trust nobody: no outdegree from the judge node
2. everyone trust judge except the judge itself: judge node will have N-1 indegree
N = 3
trust = [[1, 3], [2, 3], [3, 1]]
3. single node
N= 1
trust = []

"""
