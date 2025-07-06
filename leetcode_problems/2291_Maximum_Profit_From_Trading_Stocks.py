"""
You are given two 0-indexed integer arrays of the same length present and future where present[i] is the current price of the ith stock and future[i] is the price of the ith stock a year in the future. You may buy each stock at most once. You are also given an integer budget representing the amount of money you currently have.

Return the maximum amount of profit you can make.

 

Example 1:

Input: present = [5,4,6,2,3], future = [8,5,4,3,5], budget = 10
Output: 6
Explanation: One possible way to maximize your profit is to:
Buy the 0th, 3rd, and 4th stocks for a total of 5 + 2 + 3 = 10.
Next year, sell all three stocks for a total of 8 + 3 + 5 = 16.
The profit you made is 16 - 10 = 6.
It can be shown that the maximum profit you can make is 6.

Example 2:

Input: present = [2,2,5], future = [3,4,10], budget = 6
Output: 5
Explanation: The only possible way to maximize your profit is to:
Buy the 2nd stock, and make a profit of 10 - 5 = 5.
It can be shown that the maximum profit you can make is 5.

Example 3:

Input: present = [3,3,12], future = [0,3,15], budget = 10
Output: 0
Explanation: One possible way to maximize your profit is to:
Buy the 1st stock, and make a profit of 3 - 3 = 0.
It can be shown that the maximum profit you can make is 0.

 

Constraints:

    n == present.length == future.length
    1 <= n <= 1000
    0 <= present[i], future[i] <= 100
    0 <= budget <= 1000

"""
from functools import lru_cache
from typing import List

class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        """
        # two choice to maximize profit
        # take it and spend the budget
        # don't take it and buy the next stock
        # cache = {}

        @lru_cache(maxsize=None)
        def dp(idx, budget):
            #base case
            # if idx is out of range
            if idx >= len(present):
                return 0

            # if (idx, budget) in cache:
            #     return cache[(idx, budget)]

            # choices
            taking_current_stock = skipping_current_stock = 0
            # if choose the current index, calculate profit and budget, then move to next
            # if there is budget left, buy the stock
            if budget - present[idx] >= 0:
                taking_current_stock = (future[idx] - present[idx]) + dp(idx + 1, budget - present[idx])
            
            # nothing added, budget is same, just choose next
            skipping_current_stock = dp(idx + 1, budget)

            return max(taking_current_stock, skipping_current_stock)

            # # save in cache
            # cache[(idx, budget)] = max(taking_current_stock, skipping_current_stock)
            # return cache[(idx, budget)]

        return dp(0, budget)
        """
        

        dp = [0] * (budget+1)

        for idx in range(len(present)):

            for j in range(budget, present[idx] - 1, -1):

                dp[j] = max(
                    dp[j], 
                    dp[j - present[idx]] + future[idx] - present[idx]
                )
        
        return dp[-1]

import unittest

class TestSuite(unittest.TestCase):
    
    def test_solution(self):
        sol = Solution()
        present = [2,2,5]
        future = [3,4,10]
        budget = 6

        self.assertEqual(
            sol.maximumProfit(
                present, future, budget
            ),
            5
        )

if __name__ == "__main__":
    unittest.main()