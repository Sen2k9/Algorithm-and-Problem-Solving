

class Solution:
    def generate(self, numRows: int):
        n = numRows
        arr = []

        for i in range(0, n):
            temp = [1]*(i+1)
            for j in range(0, i):
                if i - 1 >= 0 and j - 1 >= 0:
                    temp[j] = arr[i - 1][j - 1] + arr[i-1][j]
            arr.append(temp)
        return arr


sol = Solution()
numRows = 5
print(sol.generate(numRows))

# corner case : numRows = 0,1,2

# Output:
# [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1]
# ]
