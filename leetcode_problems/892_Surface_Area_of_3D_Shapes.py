"""
On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.

 

Example 1:

Input: [[2]]
Output: 10

Example 2:

Input: [[1,2],[3,4]]
Output: 34

Example 3:

Input: [[1,0],[0,2]]
Output: 16

Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32

Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46

 

Note:

    1 <= N <= 50
    0 <= grid[i][j] <= 50


"""


class Solution:
    def surfaceArea(self, grid):
        top = 0
        for row in grid:
            for num in row:
                if num > 0:
                    top += 1

        left = 0
        for row in grid:
            seen = 0
            for num in row:
                if num - seen > 0:
                    left = left + (num - seen)
                seen = num

        front = 0
        for i in range(len(grid[0])):
            std = 0
            for row in grid:

                if row[i] - std > 0:
                    front += row[i] - std

                std = row[i]
        return 2 * (top+left+front)


sol = Solution()
grid = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
print(sol.surfaceArea(grid))
"""
corner case:
1. multiple cube touches each other

reference:
https://leetcode.com/problems/surface-area-of-3d-shapes/discuss/369902/Python-faster-than-99-compute-only-three-faces-then-get-the-answer
"""
