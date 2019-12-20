"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.

Note:

    1 <= grid.length <= 10
    1 <= grid[0].length <= 10
    0 <= grid[i][j] <= 15

"""


class Solution:
    def numMagicSquaresInside(self, grid):
        def check(arr):
            l = []
            for each in arr:
                l = l + each
            if sorted(l) != [x for x in range(1, 10)]:
                return False
            col = list(zip(arr[0], arr[1], arr[2]))
            same = sum(arr[0])
            diag1 = 0
            diag2 = 0
            for i in range(3):
                if sum(arr[i]) != same or sum(col[i]) != same:
                    return False
                diag1 = diag1 + arr[i][i]
                diag2 = diag2 + arr[i][2 - i]
            if diag1 != diag2:
                return False

            return True
        m = len(grid)
        n = len(grid[0])
        if m < 3 or n < 3:
            return 0
        count = 0
        for i in range(m - 2):
            for j in range(n - 2):
                arr = []
                arr.append(grid[i][j: j + 3])
                arr.append(grid[i + 1][j: j + 3])
                arr.append(grid[i + 2][j: j + 3])
                m = check(arr)
                if m:
                    count += 1
        return count


sol = Solution()
grid = [[4, 3, 8, 4],
        [9, 5, 1, 9],
        [2, 7, 6, 2]]

print(sol.numMagicSquaresInside(grid))
"""
corner case:
1. "3 x 3 grid filled with distinct numbers from 1 to 9" means there is total 9 distinct number 
"""
