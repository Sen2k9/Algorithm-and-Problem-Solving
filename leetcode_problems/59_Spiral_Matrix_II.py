"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

"""


class Solution:
    def generateMatrix(self, n: int):
        grid = [[0] * n for _ in range(n)]

        row_start = 0
        row_last = n - 1
        col_start = n - 1
        col_last = 0
        count = 1

        while row_start <= row_last or col_last <= col_start:

            for j in range(col_last, col_start + 1):
                grid[row_start][j] = count
                count += 1

            row_start += 1

            for i in range(row_start, row_last + 1):
                grid[i][col_start] = count
                count += 1

            col_start -= 1

            for j in range(col_start, col_last - 1, -1):
                grid[row_last][j] = count
                count += 1

            row_last -= 1

            for i in range(row_last, row_start - 1, -1):
                grid[i][col_last] = count
                count += 1

            col_last += 1

        return grid


sol = Solution()
n = 100
print(sol.generateMatrix(n))
