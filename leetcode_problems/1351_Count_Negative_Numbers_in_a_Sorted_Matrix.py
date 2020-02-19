"""
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0

Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3

Example 4:

Input: grid = [[-1]]
Output: 1

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    -100 <= grid[i][j] <= 100
"""


class Solution:
    def countNegatives(self, grid):
        # Solution 1: brute-force,
        # O(m+n)
        # m = len(grid)
        # n = len(grid[0])
        # count = 0
        # for i in range(m):
        #     for j in range(n-1, -1, -1):
        #         if grid[i][j] < 0:
        #             count += 1
        #         if grid[i][j] >= 0:
        #             break
        # return count

        # Solution 2: efficient
        # O(mlogn)
        # m = len(grid)
        # n = len(grid[0])
        # count = 0

        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] < 0:
        #             count += n - j
        #             break
        # return count

        # Solution 3: using generator

        def traverse(grid):
            m = len(grid)
            n = len(grid[0])
            for i in range(m):
                for j in range(n):
                    if grid[i][j] < 0:
                        yield n - j
                        break

        return sum(count for count in traverse(grid))


sol = Solution()
grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
print(sol.countNegatives(grid))

assert sol.countNegatives(grid) == 8

"""
reference:
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/discuss/512831/Several-Python-solutions-With-explanation
"""
