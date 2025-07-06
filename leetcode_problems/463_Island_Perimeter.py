"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:

"""
import unittest
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0:
                return 1
            
            if (r, c) in visit:
                return 0
            
            visit.add((r, c))
            # look into perimeter

            perimeter = dfs(r + 1, c)
            perimeter += dfs(r - 1, c)
            perimeter += dfs(r, c + 1)
            perimeter += dfs(r, c - 1)

            return perimeter
        
        visit = set()
        perimeter = 0
        for r in range(ROWS):
            for c in range(COLS):
                # only traverse from island
                if grid[r][c] == 1:
                    perimeter += dfs(r, c)
        
        return perimeter


class TestSuit(unittest.TestCase):
    
    def test_islandPerimeter(self):               
        sol = Solution()
        grid = [[0, 1, 0, 0],
                [1, 1, 1, 0],
                [0, 1, 0, 0],
                [1, 1, 0, 0]]

        self.assertEqual(
            sol.islandPerimeter(grid),
            16
        )

if __name__ == "__main__":
    unittest.main()

"""
corner case:
island can only be one single element
[[1]]

"""
