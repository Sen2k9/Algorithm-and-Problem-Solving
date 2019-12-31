"""
We are given a matrix with R rows and C columns has cells with integer coordinates (r, c), where 0 <= r < R and 0 <= c < C.

Additionally, we are given a cell in that matrix with coordinates (r0, c0).

Return the coordinates of all cells in the matrix, sorted by their distance from (r0, c0) from smallest distance to largest distance.  Here, the distance between two cells (r1, c1) and (r2, c2) is the Manhattan distance, |r1 - r2| + |c1 - c2|.  (You may return the answer in any order that satisfies this condition.)

Example 1:

Input: R = 1, C = 2, r0 = 0, c0 = 0
Output: [[0,0],[0,1]]
Explanation: The distances from (r0, c0) to other cells are: [0,1]

Example 2:

Input: R = 2, C = 2, r0 = 0, c0 = 1
Output: [[0,1],[0,0],[1,1],[1,0]]
Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2]
The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.

Example 3:

Input: R = 2, C = 3, r0 = 1, c0 = 2
Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2,2,3]
There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].

Note:

    1 <= R <= 100
    1 <= C <= 100
    0 <= r0 < R
    0 <= c0 < C

"""


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        # Solution 1: self
        # output = []
        # for i in range(R):
        #     for j in range(C):
        #         d = abs(i - r0) + abs(j - c0)
        #         output.append([[i, j], d])
        # out = sorted(output, key=lambda x: x[1])
        # final = [x[0] for x in out]
        # return final

        # Solution 2: using dictionary

        # output = []
        # cell_by_distance = {}
        # for i in range(R):
        #     for j in range(C):
        #         d = abs(i - r0) + abs(j - c0)
        #         if d not in cell_by_distance:
        #             cell_by_distance[d] = []

        #         cell_by_distance[d].append([i, j])

        # keys = list(cell_by_distance.keys())
        # keys.sort()
        # for k in keys:
        #     print(cell_by_distance[k])
        #     output = output + cell_by_distance[k]
        # return output

        # Solution 3: fster, simple and clean, pythonic
        def dist(points):
            p1, p2 = points
            return abs(p1 - r0) + abs(p2 - c0)
        points = [(i, j) for i in range(R) for j in range(C)]
        return sorted(points, key=dist)


sol = Solution()
R = 2
C = 3
r0 = 1
c0 = 2
print(sol.allCellsDistOrder(R, C, r0, c0))

"""
references:
https://leetcode.com/problems/matrix-cells-in-distance-order/discuss/278786/Python-1-line-sorting-based-solution
"""
