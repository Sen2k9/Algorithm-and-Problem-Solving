"""


There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have direct prerequisites, for example, to take course 0 you have first to take course 1, which is expressed as a pair: [1,0]

Given the total number of courses n, a list of direct prerequisite pairs and a list of queries pairs.

You should answer for each queries[i] whether the course queries[i][0] is a prerequisite of the course queries[i][1] or not.

Return a list of boolean, the answers to the given queries.

Please note that if course a is a prerequisite of course b and course b is a prerequisite of course c, then, course a is a prerequisite of course c.

 

Example 1:

Input: n = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: course 0 is not a prerequisite of course 1 but the opposite is true.

Example 2:

Input: n = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites and each course is independent.

Example 3:

Input: n = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]

Example 4:

Input: n = 3, prerequisites = [[1,0],[2,0]], queries = [[0,1],[2,0]]
Output: [false,true]

Example 5:

Input: n = 5, prerequisites = [[0,1],[1,2],[2,3],[3,4]], queries = [[0,4],[4,0],[1,3],[3,0]]
Output: [true,false,true,false]

 

Constraints:

    2 <= n <= 100
    0 <= prerequisite.length <= (n * (n - 1) / 2)
    0 <= prerequisite[i][0], prerequisite[i][1] < n
    prerequisite[i][0] != prerequisite[i][1]
    The prerequisites graph has no cycles.
    The prerequisites graph has no repeated edges.
    1 <= queries.length <= 10^4
    queries[i][0] != queries[i][1]


"""
from collections import defaultdict


class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites, queries):

        if not queries or len(queries) == 0 or len(queries[0]) == 0:
            return []

        ans = [False]*len(queries)

        if not prerequisites:
            return ans

        self.dic = defaultdict(set)

        for pre in prerequisites:

            self.dic[pre[1]].add(pre[0])
            if pre[0] in self.dic:
                self.dic[pre[1]] = self.dic[pre[1]] | self.dic[pre[0]]

        for i in range(len(prerequisites) - 1, -1, -1):  # not in order

            if prerequisites[i][0] in self.dic:
                self.dic[prerequisites[i][1]] = self.dic[prerequisites[i]
                                                         [1]] | self.dic[prerequisites[i][0]]

        print(self.dic)

        for i, query in enumerate(queries):
            u = query[1]
            v = query[0]
            if u < 0 or u > n-1 or v < 0 or v > n-1:
                continue

            if self.dic[u]:

                for child in self.dic[u]:

                    if child == v:
                        ans[i] = True
                        break

        return ans

    # def dfs(self, u, v):
    #     if u == v:
    #         return True

    #     if self.dic[u]:
    #         for neighbour in self.dic[u]:
    #             if self.dfs(neighbour, v):
    #                 return True
    #     else:
    #         return False


sol = Solution()

n = 5
prerequisites = [[0, 1], [3, 4], [1, 2], [2, 3]]
queries = [[0, 4], [4, 0], [1, 3], [3, 0]]
print(sol.checkIfPrerequisite(n, prerequisites, queries))
