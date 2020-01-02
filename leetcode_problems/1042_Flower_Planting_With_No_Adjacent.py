"""
You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.

paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.

Also, there is no garden that has more than 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.

Example 1:

Input: N = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]

Example 2:

Input: N = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]

Example 3:

Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]

 

Note:

    1 <= N <= 10000
    0 <= paths.size <= 20000
    No garden has 4 or more paths coming into or leaving it.
    It is guaranteed an answer exists.

"""


class Solution:
    def gardenNoAdj(self, N, paths):
        if not paths and N == 1:
            return [1]

        if len(paths) == 1 and N == 1:
            return [1]
        import collections
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        g = collections.defaultdict(list)
        plantdict = {}

        for i in range(1, N + 1):
            plantdict[i] = 0
        for a, b in paths:
            g[a].append(b)
            g[b].append(a)

        for garden in g:

            flower = set(range(1, 5))

            for neighbours in g[garden]:
                if plantdict[neighbours] != 0 and plantdict[neighbours] in flower:
                    flower.remove(plantdict[neighbours])
            plantdict[garden] = flower.pop()

        return [plantdict[x] if plantdict[x] != 0 else 1 for x in range(1, N+1)]


sol = Solution()
N = 3
paths = [[1, 2], [2, 3], [3, 1]]
print(sol.gardenNoAdj(N, paths))
"""
corner case:
1. no path
2. one garden but self loop
reference:
https://leetcode.com/problems/flower-planting-with-no-adjacent/discuss/290930/Python-Greedy-Concise-%2B-Explanation
"""
