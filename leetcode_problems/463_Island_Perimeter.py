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


class Solution:
    def islandPerimeter(self, grid):
        # solution 1: 
        # dic = {1: 3, 2: 2, 3: 1, 0:4, 4:0} # for each count exposed edges
        # total_edge = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
                
        #         if grid[i][j] == 1:
        #             count = 0

        #             for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        #                 nx = i + x
        #                 ny = j + y
        #                 if 0 <= nx and nx <= len(grid)-1 and 0 <= ny and ny <= len(grid[0])-1 and grid[nx][ny] == 1:
        #                     count += 1
                            
        #             total_edge = total_edge + dic[count]

        # return total_edge

        # Solution 2:

        total_edge = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i == 0 or grid[i - 1][j] == 0: #top side
                        total_edge += 1
                    if j == 0 or grid[i][j - 1] == 0: # left side
                        total_edge += 1

                    if j== len(grid[0])-1 or grid[i][j + 1] == 0: # right side
                        total_edge += 1
                    if i == len(grid)-1 or grid[i + 1][j] == 0: # bottom side
                        total_edge += 1
                        
        return total_edge
                    
                        
sol = Solution()
grid = [[0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]]

print(sol.islandPerimeter(grid))


"""
idea:
if a land cell connected with another one land block, three edges exposed
if a land cell connected with another two land block, two edges exposed
if a land cell connected with another three land block, one edge exposed
if a land cell not connected with any other land block, four edges exposed

corner case:
island can only be one single element
[[1]]

"""
