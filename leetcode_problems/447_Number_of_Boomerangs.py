"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""


class Solution:
    def numberOfBoomerangs(self, points):
        import math

        def get_distance(p1, p2):
            return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

        res = 0
        for i in range(len(points)):
            dic = {}
            for j in range(len(points)):
                if i == j:
                    continue
                d = get_distance(points[i], points[j])
                if d not in dic:
                    dic[d] = 1
                else:
                    dic[d] += 1
            for key, value in dic.items():
                # print(value)
                res = value * (value - 1) + res
            print(dic)
        return res


sol = Solution()
points = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]
print(sol.numberOfBoomerangs(points))
