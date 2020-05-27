"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.

Given target = 20, return false.
"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Solutoin 1: using bfs
        # check = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # from collections import deque
        # if matrix[0][0] == target:
        #     return True
        # queue = deque([(0, 0)])
        # #queue.append((0, 0))
        # visited = set((0, 0))
        # m = len(matrix) - 1
        # n = len(matrix[0])-1
        # while queue:
        #     r, c = queue.popleft()
        #     for i, j in check:
        #         rr = r + i
        #         cc = c + j
        #         if rr >= 0 and rr <= m and cc >= 0 and cc <= n:
        #             if matrix[rr][cc] == target:
        #                 return True
        #             if (rr, cc) not in visited:
        #                 queue.append((rr, cc))
        #                 visited.add((rr, cc))
        #     # print(queue)
        # return False

        # Solution 2: using binary search
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        def binary_search(values, target):
            low = 0
            high = len(values) - 1
            while low < high:
                mid = (low + high) // 2
                if values[mid] == target:
                    return True
                elif values[mid] > target:
                    high = mid
                else:
                    low = mid+1

            return values[low] == target
        # if n == 1:
        #     values = list(zip(*matrix))
        #     # print(values)
        #     return binary_search(values, target)
        # else:
        for each in matrix:
            if binary_search(each, target):
                return True
        return False


sol = Solution()
# m = [
#     [1,   4,  7, 11, 15],
#     [2,   5,  8, 12, 19],
#     [3,   6,  9, 16, 22],
#     [10, 13, 14, 17, 24],
#     [18, 21, 23, 26, 30]
# ]
m = [[-5]]
target = -5

print(sol.searchMatrix(m, target))
"""
corner case:
1. []
2. [[]]
3. [[1,2,3,4,5]]
4. [[1], [2],[3],[4],[5]]
"""
