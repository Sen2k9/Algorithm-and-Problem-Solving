"""
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation: 
The five points are show in the figure below. The red triangle is the largest.

Notes:

    3 <= points.length <= 50.
    No points will be duplicated.
     -50 <= points[i][j] <= 50.
    Answers within 10^-6 of the true value will be accepted as correct.

"""


class Solution:
    def largestTriangleArea(self, points):
        # O(n^3)
        import math
        result = 0

        def area(x, y, z):
            a = math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)
            b = math.sqrt((y[0] - z[0]) ** 2 + (y[1] - z[1]) ** 2)
            c = math.sqrt((x[0] - z[0]) ** 2 + (x[1] - z[1]) ** 2)
            s = (a + b + c) / 2
            # only sqrt can create complex number. in that case leaving 0 is removes runtime complexity
            # Heron's Formula for the area of a triangle
            return (max(0, (s * (s - a) * (s - b) * (s - c))))**0.5

        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                for k in range(j + 1, len(points)):
                    a = area(points[i], points[j], points[k])
                    result = max(result, a)
        return result


sol = Solution()
points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
print(sol.largestTriangleArea(points))
"""
https://www.mathopenref.com/heronsformula.html
"""
