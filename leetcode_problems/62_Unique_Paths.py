"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

 

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:

Input: m = 7, n = 3
Output: 28

 

Constraints:

    1 <= m, n <= 100
    It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

"""


class Solution:
    def uniquePaths(self, m: int, n: int):
        from collections import deque
        queue = deque()
        queue.append((0, 0))
        path = 0
        check = [(1, 0), (0, 1)]

        while queue:
            i, j = queue.popleft()
            for k, l in check:
                new_i = i+k
                new_j = j + l
                if new_i >= 0 and new_i <= m - 1 and new_j >= 0 and new_j <= n - 1:
                    if new_i == m - 1 and new_j == n - 1:
                        path += 1
                    else:
                        queue.append((new_i, new_j))
        return path


sol = Solution()
m = 7
n = 3
print(sol.uniquePaths(m, n))
"""
corner case:
m=1
n=1
"""
