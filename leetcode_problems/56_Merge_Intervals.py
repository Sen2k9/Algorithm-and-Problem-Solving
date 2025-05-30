"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

Constraints:

    intervals[i][0] <= intervals[i][1]

"""
import unittest
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))

        stack = []

        for interval in intervals:

            if stack and stack[-1][1] >= interval[0]:
                stack[-1] = [
                    min(stack[-1][0], interval[0]),
                    max(stack[-1][1], interval[1])
                ]
            
            else:
                stack.append(interval)
        
        return stack

class TestSuite(unittest.TestCase):
    
    def test_merge(self):
        sol = Solution()
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        self.assertEqual(
            sol.merge(intervals),
            [[1,6],[8,10],[15,18]]
        )

        # intervals = [[1,4],[4,5]]
        # print(sol.merge(intervals))

        # intervals = [[1,3]]
        # print(sol.merge(intervals))

        # intervals = [[1,3], [1,3], [1,3], [1,3]]
        # print(sol.merge(intervals))

        # intervals = [[1,3], [4,6], [7,9], [10,30]]
        # print(sol.merge(intervals))

        # intervals = [[1, 5], [10, 12], [3, 7], [15, 17], [8, 13]]
        # print(sol.merge(intervals))

        # intervals = [[1,1], [3,3], [1,3], [1,3]]
        # print(sol.merge(intervals))

        # intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
        # print(sol.merge(intervals))


        # intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
        # print(sol.merge(intervals))

if __name__ == "__main__":
    unittest.main()