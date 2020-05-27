class Solution:
    def rotateMatrix(self, matrix):
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        n = len(matrix)

        # for r in range(n):
        #     for c in range(n):
        #         if r + c < n:
        #             matrix[n - 1 - c][n - 1 -
        #                               r], matrix[r][c] = matrix[r][c], matrix[n - 1 - c][n - 1 - r]
        #         else:
        #             break
        # # print(matrix)

        # for r in range(n):
        #     for c in range(n):
        #         if n - 1 - r >= r:
        #             matrix[n - 1 - r][c], matrix[r][c] = matrix[r][c], matrix[n - 1 - r][c]

        #         else:
        #             break

        # return matrix

        for layer in range(n // 2):

            first = layer
            last = n - 1 - layer

            for i in range(first, last):
                offset = i - first

                top = matrix[first][i]
                # left -> top

                matrix[first][i] = matrix[last-offset][first]

                # bottom -> left

                matrix[last - offset][first] = matrix[last][last - offset]

                # right -> bottom

                matrix[last][last - offset] = matrix[i][last]

                # top -> right

                matrix[i][last] = top

            print(matrix)

        # return matrix


sol = Solution()
# matrix = [[i+j for i in range(1, 5)] for j in range(0, 13, 4)]

matrix = [[i+j for i in range(1, 4)] for j in range(0, 7, 3)]
print(matrix)
print(sol.rotateMatrix(matrix))
