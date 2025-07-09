"""
    There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.

    For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.

Return an integer array answer where answer[i] is the answer to the ith query.

 

Example 1:
ex-1

Input: s = "**|**|***|", queries = [[2,5],[5,9]]
Output: [2,3]
Explanation:
- queries[0] has two plates between candles.
- queries[1] has three plates between candles.

Example 2:
ex-2

Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
Output: [9,0,0,0,0]
Explanation:
- queries[0] has nine plates between candles.
- The other queries have zero plates between candles.

 

Constraints:

    3 <= s.length <= 105
    s consists of '*' and '|' characters.
    1 <= queries.length <= 105
    queries[i].length == 2
    0 <= lefti <= righti < s.length

"""
from typing import List

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        nearestLeftCandle = [-1] * len(s) 
        nearestRightCandle = [-1] * len(s)

        candleCount = [0] * len(s)

        # this function captures nearest left candle for current position
        candle = -1
        for idx in range(len(s)):
            if s[idx] == "|":
                candle = idx # update candle position

            nearestLeftCandle[idx] = candle

        # this function captures nearest right candle for current position
        candle = -1
        for idx in range(len(s) - 1, -1, -1):
            if s[idx] == "|":
                candle = idx # update candle position

            nearestRightCandle[idx] = candle
        
        # this function counts total candle as prefix sum
        candle = 0
        for idx in range(len(s)):
            if s[idx] == "|":
                candle += 1 

            candleCount[idx] = candle
        
        result = []

        for start, end in queries:

            left_candle = nearestRightCandle[start] # get nearest right from start
            right_candle = nearestLeftCandle[end] # get nearest left from end

            # if either left or right candle not present in the substring
            if left_candle == -1 or right_candle == -1:
                result.append(0)
            
            elif left_candle >= right_candle:
                result.append(0)
            
            else:
                # plate count is the difference of candle count from full range of eligible string
                result.append(
                    (right_candle - left_candle + 1)
                    - (candleCount[right_candle] - candleCount[left_candle] + 1)
                )
        
        return result

import unittest

class TestSuite(unittest.TestCase):
    
    def test_platesBetweenCandles(self):
        sol = Solution()
        s = "***|**|*****|**||**|*"
        queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
        
        self.asssetEqual(
            sol.platesBetweenCandles(
                s,
                queries
            ),
            [9,0,0,0,0]
        )

if __name__ == "__main__":
    
    unittest.main()
