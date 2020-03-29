"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:

Input: [[7,10],[2,4]]
Output: 1

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""


class Solution:
    def minMeetingRooms(self, intervals):
        start_time = []
        end_time = []
        for each in intervals:
            start_time.append(each[0])
            end_time.append(each[1])

        start_time.sort()
        end_time.sort()
        total_rooms = 0
        i = 0
        j = 0
        while i < len(start_time):
            if start_time[i] < end_time[j]:
                total_rooms += 1
            else:
                j += 1
            i += 1

        return total_rooms


sol = Solution()
n = [[9, 10], [4, 9], [4, 17]]

print(sol.minMeetingRooms(n))
