"""
A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true

Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false

Notes:

    Both rectangles rec1 and rec2 are lists of 4 integers.
    All coordinates in rectangles will be between -10^9 and 10^9.
"""


class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        # Solution 1:
        # x1, y1, x2, y2 = rec1[0], rec1[1], rec1[2], rec1[3]
        # x3, y3, x4, y4 = rec2[0], rec2[1], rec2[2], rec2[3]

        # width = min(x4, x2) - max(x3, x1)
        # height = min(y4, y2)-max(y1, y3)

        # # if two rectangle touch then width and height will be zero, which is not allowed
        # # to overlap the width and height have to be greater than zero

        # return width > 0 and height > 0

        # Solution 2: faster
        x1, y1, x2, y2 = rec1[0], rec1[1], rec1[2], rec1[3]
        x3, y3, x4, y4 = rec2[0], rec2[1], rec2[2], rec2[3]
        if x4 <= x1 or y4 <= y1 or x2 <= x3 or y2 <= y3:
            return False
        else:
            return True


sol = Solution()
rec1 = [0, 0, 1, 1]
rec2 = [1, 0, 2, 1]
print(sol.isRectangleOverlap(rec1, rec2))

"""
reference:
https://leetcode.com/problems/rectangle-overlap/discuss/480808/Python3-beats-100-solution-with-explanations
https://leetcode.com/problems/rectangle-overlap/discuss/349856/Python3-False-scenario

"""
