"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""


class Solution:
    def searchMatrix(self, matrix, target):

        if not matrix:
            return False

        if not matrix[0]:
            return False

        if target < matrix[0][0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        if target > matrix[m-1][n-1]:
            return False

        low = 0
        high = m*n

        while low <= high:

            mid = (low+high)//2

            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                low = mid + 1

            elif matrix[row][col] > target:
                high = mid - 1

        return False


sol = Solution()
matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
target = 3
print(sol.searchMatrix(matrix, target))
