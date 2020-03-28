"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""


class Solution:
    def numIslands(self, grid):
        num_of_island = 0
        check = [[0, 1], [1, 0]]
        m = len(grid) - 1
        n = len(grid[0])-1

        def bfs(row, col, grid):
            from collections import deque
            queue = deque()
            queue.append([row, col])
            grid[row][col] = 0
            while queue:
                row, col = queue.popleft()

                for k, l in check:
                    rr = row + k
                    cc = col + l
                    if rr >= 0 and rr <= m and cc >= 0 and cc <= n:
                        if grid[rr][cc] == "1":

                            queue.append([rr, cc])
                            grid[rr][cc] = 0
            # print(grid)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num_of_island += 1
                    # print(grid)
                    bfs(i, j, grid)

        return num_of_island


sol = Solution()
n = [["1", "1", "0", "0", "0"],
     ["1", "1", "0", "0", "0"],
     ["0", "0", "1", "0", "0"],
     ["0", "0", "0", "1", "1"]
     ]
print(sol.numIslands(n))

"""
[["1","1","1"],["0","1","0"],["1","1","1"]]

"""
