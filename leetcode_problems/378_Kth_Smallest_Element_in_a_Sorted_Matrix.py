"""
"""


class Solution:
    def kthSmallest(self, matrix, k):
        import heapq
        ans = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                heapq.heappush(ans, -matrix[j][i])
                print(ans)
                if len(ans) > k:
                    heapq.heappop(ans)
        return -heapq.heappop(ans)


sol = Solution()
matrix = [
    [1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 4
print(sol.kthSmallest(matrix, k))
