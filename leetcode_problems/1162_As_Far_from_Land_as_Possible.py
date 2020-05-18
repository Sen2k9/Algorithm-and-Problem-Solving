"""
Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.

 

Example 1:

Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.

Example 2:

Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.

 

Note:

    1 <= grid.length == grid[0].length <= 100
    grid[i][j] is 0 or 1


"""

from collections import deque


class Solution:
    def maxDistance(self, grid):

        all_ones = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    all_ones.append((i, j, 0))

        if not all_ones or len(all_ones) == len(grid) ** 2:
            return - 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        d = 0

        while all_ones:
            i, j, d = all_ones.popleft()

            for x, y in directions:
                ix = i + x
                jy = j + y

                # if I can overwrite the values
                if ix >= 0 and ix <= len(grid) - 1 and jy >= 0 and jy <= len(grid[0]) - 1 and grid[ix][jy] != 1:

                    all_ones.append((ix, jy, d + 1))

                    grid[ix][jy] = 1

        return d


sol = Solution()
grid = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
print(sol.maxDistance(grid))
