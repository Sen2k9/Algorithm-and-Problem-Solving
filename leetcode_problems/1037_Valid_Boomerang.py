"""
A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.

Example 1:

Input: [[1,1],[2,3],[3,2]]
Output: true

Example 2:

Input: [[1,1],[2,2],[3,3]]
Output: false

Note:

    points.length == 3
    points[i].length == 2
    0 <= points[i][j] <= 100
"""


class Solution:
    def isBoomerang(self, points):
        A, B, C = points
        AB = ((A[0] - B[0])**2 + (A[1] - B[1])**2)**(0.5)
        BC = ((B[0] - C[0])**2 + (B[1] - C[1])**2)**(0.5)
        AC = ((A[0] - C[0])**2 + (A[1] - C[1])**2)**(0.5)
        return not(AB == BC + AC or BC == AB + AC or AC == AB + BC)


sol = Solution()
print(sol.isBoomerang([[1, 1], [2, 2], [3, 3]]))
