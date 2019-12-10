class Solution:
    """
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


"""

    def maxProfit(self, prices):
        buy = float("Inf")
        maxProfit = 0
        for each in prices:
            if each < buy:  # captures the case of choosing the minimum stock as buying price
                buy = each
            elif each - buy > maxProfit:  # capture the case of not using previous day stock as selling price +
                # using last day(e.g. n-1) minimum price as buying price +
                # choosing the maximum profit price only
                maxProfit = each - buy
        return maxProfit


sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(sol.maxProfit(prices))
"""
corner case:
cannot buy stock at the last day and sell at the first day
prices = [2, 3, 4, 5, 1] # lowest price on last day
prices = [2,1,2,0,1] # maximum profit if previous day sell price use to calculate profit : prices[2]-prices[3]
prices = [7,6,4,3,1] # no selling day available
prices = [7,1,5,3,6,4]
"""
