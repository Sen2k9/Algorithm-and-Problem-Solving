"""
In a given grid, each cell can have one of three values:

    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.


Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

 

Note:

    1 <= grid.length <= 10
    1 <= grid[0].length <= 10
    grid[i][j] is only 0, 1, or 2.


"""


class Solution:
    def orangesRotting(self, grid):
        rotten = []
        fresh = 0
        minute = 0

        # at first find out which orange are already rotten
        # O(n)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        # for every already rotten orange, make all fresh orange in 4-direction of them rotten and add the new rotten orange in the rotten list
        # by this process we will end up rotting all fresh orange
        # O(n)
        while rotten:
            print(rotten)
            new_rotten = []
            for i, j in rotten:
                for x, y in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                    nx = i + x
                    ny = j + y
                    if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        new_rotten.append((nx, ny))

            rotten = new_rotten

            if rotten:
                minute += 1

        if not fresh:
            return minute
        else:
            return -1


sol = Solution()
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(sol.orangesRotting(grid))
