"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

Example 4:

Input: coins = [1], amount = 1
Output: 1

Example 5:

Input: coins = [1], amount = 2
Output: 2

Constraints:

    1 <= coins.length <= 12
    1 <= coins[i] <= 231 - 1
    0 <= amount <= 231 - 1

"""

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if not amount:
            return 0
        if not coins:
            return -1
        
        dp_array = [amount + 1] * (amount + 1)
        dp_array[0] = 0

        for value in range(1, amount + 1): # N
            for coin in coins: # C
                if coin <= value:
                    dp_array[value] = min(1 + dp_array[value - coin], dp_array[value])

        #print(dp_array)

        return dp_array[-1] if dp_array[-1] != (amount + 1) else -1




        
        




sol = Solution()

coins = [1,3,5]
amount = 11
print(sol.coinChange(coins, amount))

coins = [2]
amount = 3
print(sol.coinChange(coins, amount))

coins = [1]
amount = 0
print(sol.coinChange(coins, amount))


coins = []
amount = 1
print(sol.coinChange(coins, amount))

coins = [2,5,10,1]
amount = 27
print(sol.coinChange(coins, amount))

coins = [186,419,83,408]
amount = 6249
print(sol.coinChange(coins, amount))