"""
Write an algorithm such that if an element is an M*N matrix is 0, its entire row and column are set to 0.
"""


class Solution:

    def zeroMatrix(self, matrix):
        # Optimized solution
        # time : O(m*n)
        # Space : O(1), this method helpful for large scale system
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        firstRow = False
        firstCol = False

        non_zero = False

        m = len(matrix)
        n = len(matrix[0])

        # check first row
        for i in range(n):
            if matrix[0][i] == 0:
                firstRow = True
                break

        # check first col
        for i in range(m):
            if matrix[i][0] == 0:
                firstCol = True
                break

        if not firstRow and not firstCol:
            non_zero = True

        # check rest of the matrix for zero
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

                elif not non_zero:
                    non_zero = True

        if not non_zero:
            return matrix

        # nulify row
        for i in range(m):
            if matrix[i][0] == 0:
                self.nulifyRow(matrix, i, n)

        # nulify col
        for j in range(n):
            if matrix[0][j] == 0:
                self.nulifyCol(matrix, j, m)

        # if first row has zero
        if firstRow:
            self.nulifyRow(matrix, 0, n)

        # if first col has zero

        if firstCol:
            self.nulifyCol(matrix, 0, m)

        return matrix

    def nulifyRow(self, matrix, row, n):
        for j in range(n):
            matrix[row][j] = 0

    def nulifyCol(self, matrix, col, m):
        for i in range(m):
            matrix[i][col] = 0


sol = Solution()

matrix = [[1, 0, 1, 1, 2],

          [1, 1, 1, 1, 1],
          [2, 2, 0, 3, 4]]

print(sol.zeroMatrix(matrix))
