"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""


class Solution:
    def spiralOrder(self, matrix):

        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        m = len(matrix)
        n = len(matrix[0])

        ans = []
        layers = 0

        if n % 2 == 0:
            layers = n // 2
        else:
            layers = n // 2 + 1

        for layer in range(layers):

            # top -> right
            start = layer
            end = n - 1 - layer
            r = layer
            if len(ans) != m * n:
                for c in range(start, end + 1):
                    ans.append(matrix[r][c])

            # right -> bottom

            start = layer + 1
            end = m - 1 - layer

            c = n - 1 - layer

            if len(ans) != m * n:
                for r in range(start, end + 1):
                    ans.append(matrix[r][c])

            # bottom -> left

            start = n - 2 - layer
            end = layer

            r = m - 1 - layer
            if len(ans) != m * n:
                for c in range(start, end - 1, -1):
                    ans.append(matrix[r][c])

            # left -> top

            start = m - 2 - layer
            end = layer + 1

            c = layer
            if len(ans) != m * n:
                for r in range(start, end - 1, -1):
                    ans.append(matrix[r][c])

            if len(ans) == m * n:
                return ans

        return ans


sol = Solution()
# matrix = [
#     [1],
#     [5],
#     [9],
#     [11],
#     [13]
# ]
matrix = [[1, 2, 3, 4, 5]]
print(sol.spiralOrder(matrix))

"""
Time-complexity : O(n)
Space - complexity : O(1)
this problem takes the concept of LC#498 : Diagonal Traverse
"""
