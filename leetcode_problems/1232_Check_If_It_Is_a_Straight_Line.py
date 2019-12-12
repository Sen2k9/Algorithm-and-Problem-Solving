"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:

    2 <= coordinates.length <= 1000
    coordinates[i].length == 2
    -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    coordinates contains no duplicate point.

"""


class Solution:
    def checkStraightLine(self, coordinates):
        # solution1:

        # prev = coordinates[0]
        # present = coordinates[1]
        # x = set(elem[0] for elem in coordinates)
        # y = set(elem[1] for elem in coordinates)
        # print((x))
        # print((y))
        # if len(x) != len(y):
        #     if len(x) == 1 or len(y) == 1:
        #         return True
        #     return False

        # slope = (present[1] - prev[1]) / (present[0] - prev[0])
        # for i in range(2, len(coordinates)):
        #     present = coordinates[i]
        #     temp = (present[1] - prev[1]) / (present[0] - prev[0])
        #     if temp != slope:
        #         return False
        #     slope = temp
        # return True

        # solution 2 (More pythonic):
        (x1, y1), (x2, y2) = coordinates[:2]
        #print(coordinates[:2], coordinates[2:])
        return all((y1-y2)*(x1-x3) == (y1-y3) * (x1-x2) for x3, y3 in coordinates[2:])


sol = Solution()
coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
print(sol.checkStraightLine(coordinates))

"""
corner case:
1. zero division error:
[[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]

2. line parallel to x-axis or y-axis:
either all x points has one value or y points has one value
"""
"""
Efficient Solution
basic math:
if three points need to be in straight line: 
Basically, we are checking that the slopes between point 1 and point 2 and point 1 and point 3 match. Slope is change in y divided by change in x, so we have:

y1 - y2     y1 - y3
-------  =  --------
x1 - x2     x1 - x3

Cross multiplying gives (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2) to avoid Division by zero error
References:
https://www.geeksforgeeks.org/program-check-three-points-collinear/
https://stackoverflow.com/questions/3813681/checking-to-see-if-3-points-are-on-the-same-line

"""
