"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.



Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

Note:

The total number of elements of the given matrix will not exceed 10,000.

"""


class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        m = len(matrix)
        n = len(matrix[0])

        if m == 1:
            return matrix[0]

        ans = []

        if n == 1:
            for i in range(m):
                ans.append(matrix[i][0])
            return ans

        row = 0
        column = 0
        direction = 1

        while row < m and column < n:
            ans.append(matrix[row][column])

            if direction:
                new_row = row - 1
                new_column = column + 1

            else:

                new_row = row + 1
                new_column = column - 1

            if new_row < 0 or new_row == m or new_column < 0 or new_column == n:

                if direction:
                    new_row = row + (1 if column == n - 1 else 0)
                    new_column = column + (1 if column < n - 1 else 0)

                else:
                    new_row = row + (0 if row == m - 1 else 1)
                    new_column = column + (0 if row < m - 1 else 1)

                direction = 0 if direction else 1

            row = new_row
            column = new_column

        return ans


sol = Solution()
# matrix = [
#     [1, 2, 3, 10],
#     [4, 5, 6, 11],
#     [7, 8, 9, 12]
# ]
#matrix = [[6, 9, 7]]
matrix = [[6], [9], [7]]
#matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
print(sol.findDiagonalOrder(matrix))
print(sol.findDiagonalOrder([]))
print(sol.findDiagonalOrder(None))
print(sol.findDiagonalOrder([[]]))
