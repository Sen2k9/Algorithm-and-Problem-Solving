"""
There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

Example 1:

Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.

Example 2:

Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
Output: 5
Explanation: There are 5 roads that are connected to cities 1 or 2.

Example 3:

Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
Output: 5
Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.

Constraints:

    2 <= n <= 100
    0 <= roads.length <= n * (n - 1) / 2
    roads[i].length == 2
    0 <= ai, bi <= n-1
    ai != bi
    Each pair of cities has at most one road connecting them.

"""
from collections import defaultdict


class Solution:
    def maximalNetworkRank(self, n: int, roads) -> int:
        adjacency_list = defaultdict(set)
        for road in roads:
            adjacency_list[road[0]].add(road[1])
            adjacency_list[road[1]].add(road[0])

        # adjacency_list = \
        #     sorted(adjacency_list.items(), key=lambda x: len(x[1]), reverse=True)

        #print(adjacency_list)
        max_rank = 0
        local_rank = 0
        # for i in range(len(adjacency_list)-1):
        #     local_rank = len(adjacency_list[i][1])\
        #                  + len(adjacency_list[i+1][1])

        #     if adjacency_list[i][0] in adjacency_list[i+1][1]:
        #         local_rank -= 1

        #     max_rank = max(max_rank, local_rank)

        for i in range(n):
            
            for j in range(i+1, n):
                local_rank = len(adjacency_list[i]) \
                             + len(adjacency_list[j])
                if i in adjacency_list[j]:
                    local_rank -= 1

                max_rank = max(max_rank, local_rank)
                local_rank = 0

        return max_rank
            





sol = Solution()

n = 4
roads = [[0,1],[0,3],[1,2],[1,3]]
print(sol.maximalNetworkRank(n, roads))

n = 5
roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
print(sol.maximalNetworkRank(n, roads))

n = 8
roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
print(sol.maximalNetworkRank(n, roads))