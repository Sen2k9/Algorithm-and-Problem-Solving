
class Solution:
    def __init__(self):
        self.dp = []
        self.weight = []
        self.profits = []

    def non_repeatable_knapsack_problem(self, weights, profits, total_capacity):
        self.dp = [[0 for _ in range(total_capacity + 1)] for _ in range(len(weights) + 1)]
        self.profits = profits
        self.weight = weights

        for idx, weight in enumerate(weights, 1):
            for capacity in range(total_capacity + 1):
                if weight > capacity:
                    self.dp[idx][capacity] = self.dp[idx - 1][capacity]
                else:
                    self.dp[idx][capacity] = max(
                        self.dp[idx - 1][capacity],
                        self.dp[idx - 1][capacity - weight] + profits[idx - 1]
                    )
        return self.dp[-1][-1]

    def find_items(self):
        ans = []
        i = len(self.dp) - 1
        j = len(self.dp[0]) - 1

        profit = self.dp[-1][-1]

        while profit:
            if self.dp[i-1][j] == self.dp[i][j]:
                i -= 1
            else:
                # add the item
                ans.append(i - 1)
                # subtract the item value
                profit = profit - self.profits[i - 1]
                # subtract the item weight
                j = j - self.weight[i - 1]
        return ans




import unittest

class TestSolutoin(unittest.TestCase):

    def test_non_repeatable_knapsack_problem(self):
        weights = [1, 2, 3, 5]
        profits = [1, 6, 10, 16]

        sol = Solution()
        self.assertEqual(
            sol.non_repeatable_knapsack_problem(
                weights,
                profits,
                7
            ),
            22
        )

        self.assertEqual(
            sol.non_repeatable_knapsack_problem(
                weights,
                profits,
                6
            ),
            17
        )
    
    def test_find_items(self):
        weights = [1, 2, 3, 5]
        profits = [1, 6, 10, 16]

        sol = Solution()
        sol.non_repeatable_knapsack_problem(
            weights,
            profits,
            7
        )
        self.assertEqual(
            sol.find_items(),
            [3, 1]
        )

if __name__ == '__main__':
    unittest.main()