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


class Solution:
    def merge(self, intervals):
        # Solution 1: sorting, two-pointer: O(nlogn), O(n)
        # corner case
        # if not intervals or len(intervals) == 1:
        #     return intervals
        # # nlogn time
        # intervals = sorted(intervals, key=lambda items: (items[0], items[1]))
        # # use two-pointer to merge adjacent intervals
        # result = [intervals[0]]  # O(n) space
        # first_pointer = 0
        # second_pointer = 1
        # while second_pointer < len(intervals):
        #     if intervals[second_pointer][0] <= result[first_pointer][1]:
        #         result[first_pointer] = [min(result[first_pointer][0], intervals[second_pointer][0]),
        #         max(result[first_pointer][1], intervals[second_pointer][1])]
        #     else:
        #         result.append(intervals[second_pointer])
        #         first_pointer += 1
        #     second_pointer += 1
        # return result

        # Solution 2: Optimal: time O(nlogn), Space O(1)

        if not intervals or len(intervals) == 1:
            return intervals

        intervals = sorted(intervals, 
        key=lambda items: (items[0], items[1]))


        pointer1 = 0

        pointer2 = 1

        while pointer2 < len(intervals):
            if intervals[pointer1][1] >= intervals[pointer2][0]:
                intervals[pointer1] = [min(intervals[pointer1][0], intervals[pointer2][0]),
                max(intervals[pointer1][1], intervals[pointer2][1])]

            else:
                pointer1 += 1
                intervals[pointer1] = intervals[pointer2]  # in-place replace

            pointer2 += 1

            #print(intervals, pointer1, pointer2)

        return intervals[:pointer1+1]



sol = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(sol.merge(intervals))

intervals = [[1,4],[4,5]]
print(sol.merge(intervals))

intervals = [[1,3]]
print(sol.merge(intervals))

intervals = [[1,3], [1,3], [1,3], [1,3]]
print(sol.merge(intervals))

intervals = [[1,3], [4,6], [7,9], [10,30]]
print(sol.merge(intervals))

intervals = [[1, 5], [10, 12], [3, 7], [15, 17], [8, 13]]
print(sol.merge(intervals))

intervals = [[1,1], [3,3], [1,3], [1,3]]
print(sol.merge(intervals))

intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
print(sol.merge(intervals))


intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
print(sol.merge(intervals))