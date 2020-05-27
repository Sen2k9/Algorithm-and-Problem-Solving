"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:

    A straight forward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?
"""


class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # row = set()
        # col = set()
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):

        #         if matrix[i][j] == 0:
        #             row.add(i)
        #             col.add(j)

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if i in row or j in col:
        #             matrix[i][j] = 0

        # return matrix

        # Solution 2:
        # for i in range(len(matrix)):
        #     found = False
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == 0:
        #             found = True
        #             break
        #     if found:
        #         for j in range(len(matrix[0])):
        #             if matrix[i][j] != 0:
        #                 matrix[i][j] = "z"

        # for j in range(len(matrix[0])):
        #     found = False
        #     for i in range(len(matrix)):
        #         if matrix[i][j] == 0:
        #             found = True
        #             break

        #     if found:
        #         for i in range(len(matrix)):
        #             if matrix[i][j] != 0:
        #                 matrix[i][j] = "z"

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == "z":

        #             matrix[i][j] = 0

        # return matrix
        # Solution 3:
        zero_col = False
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][0] == 0:
                zero_col = True
            for j in range(n):

                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        print(matrix, zero_col)

        # for j in range(1, n):
        #     if matrix[0][j] == 0:

        #         for i in range(1, m):
        #             matrix[i][j] = 0
        # print(matrix)
        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][0] or not matrix[0][j]:

                    matrix[i][j] = 0

        print(matrix)
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        if zero_col:
            for i in range(m):
                matrix[i][0] = 0
        print(matrix)


sol = Solution()
m = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]


print(sol.setZeroes(m))
