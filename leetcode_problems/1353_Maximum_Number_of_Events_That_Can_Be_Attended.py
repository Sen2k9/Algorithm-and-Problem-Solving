"""
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startDayi <= d <= endDayi. You can only attend one event at any time d.

Return the maximum number of events you can attend.

Example 1:

Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.

Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4

Constraints:

    1 <= events.length <= 105
    events[i].length == 2
    1 <= startDayi <= endDayi <= 105

"""
from typing import List
import unittest
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        event_id = cnt = 0
        day = 1

        events = sorted(events)
        total_days = max(event[1] for event in events)
        min_heap = []

        while day <= total_days:

            # if the first start day is not exactly 1
            if event_id < len(events) and not min_heap:
                day = events[event_id][0]
            
            # all events start less or equal to current day push them to heap
            while event_id < len(events) and events[event_id][0] <= day:
                heapq.heappush(min_heap, events[event_id][1])
                event_id += 1 # increment the event
            
            # drop the events which ends before current day
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            
            # attend the event which has earliest end date
            if min_heap:
                heapq.heappop(min_heap)
                cnt += 1 # event which we can attend
            
            elif event_id >= len(events):
                break
            
            day += 1
        
        return cnt
            

class TestSuite(unittest.TestCase):
    
    def test_maxEvents(self):
        
        sol = Solution()
        events = [[1,2],[2,3],[3,4]]
        self.assertEqual(
            sol.maxEvents(events),
            3
        )

if __name__ == "__main__":
    
    unittest.main()