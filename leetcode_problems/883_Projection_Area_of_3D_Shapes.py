"""
On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Now we view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane. 

Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.

 

Example 1:

Input: [[2]]
Output: 5

Example 2:

Input: [[1,2],[3,4]]
Output: 17
Explanation: 
Here are the three projections ("shadows") of the shape made with each axis-aligned plane.

Example 3:

Input: [[1,0],[0,2]]
Output: 8

Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 14

Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 21

 
Note:

    1 <= grid.length = grid[0].length <= 50
    0 <= grid[i][j] <= 50

"""


class Solution:
    def projectionArea(self, grid):
        # Solution 1: self
        # O(n^2)
        top = 0
        right = 0
        front = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    top += 1

        for i in range(len(grid)):
            temp = 0
            for j in range(len(grid[i])):
                if grid[i][j] > temp:
                    temp = grid[i][j]
            right = right + temp

        for j in range(len(grid[0])):
            temp = 0
            for i in range(len(grid)):
                if grid[i][j] > temp:
                    temp = grid[i][j]
            front = front + temp

        return top + right + front

        # Solution 2: concise but same runing time
        # count = 0
        # rot_grid = list(zip(*grid))
        # print(rot_grid)
        # for i in range(len(grid)):
        #     count += max(grid[i])
        #     count += max(rot_grid[i])
        #     for j in range(len(grid[0])):
        #         if grid[i][j] > 0:
        #             count += 1
        # return count

        # Solution 3: using map function
        # numTop = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] != 0:
        #             numTop += 1
        # numFront = sum(map(max, grid))
        # numSide = sum(map(max, zip(*grid)))

        # return numTop+numFront+numSide


sol = Solution()
grid = [[1, 0], [0, 2]]
print(sol.projectionArea(grid))

"""
Algo:
xy projection counts non-zero entries in matrix
zx projection reflects sum of maximum elements in each row
yz projection reflects sum of maximum elements in each column
"""
