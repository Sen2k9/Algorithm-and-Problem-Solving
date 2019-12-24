"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.


"""


class Solution:
    def rob(self, nums):
        # Solution 1: self
        # n = len(nums)
        # if n == 1 or n == 2:
        #     return max(nums)
        # if n == 0:
        #     return 0
        # dp = [0] * (n)
        # dp[0] = nums[0]
        # money = nums[0]
        # max_so_far = nums[0]
        # for i in range(1, n):
        #     dp[i] = max(max_so_far, money, nums[i] + dp[i - 2])
        #     if dp[i] > money:
        #         money = dp[i]
        #     if nums[i] > max_so_far:
        #         max_so_far = nums[i]

        #     print(dp, max_so_far, money)
        # return money

        # Solution 2: efficient, rolling arrays
        """
        You cannot rob house i if you have robbed house i-1. In the stock problem, you can not buy if you have just sold. 
        This means the transition from optimal solution at i-1 to optimal solution at i, depends on the action you took at i-1. 
        This is a hint that for dynamic programming the number of states you need is the number of actions you can take at each step. 
        Here at each i, you can choose to rob or leave it. 
        Now let rob[i] be the maximal amount you can collect up to house i while robbing house i and let leave[i] be the maximal amount you can collect up to house i while leaving house i alone. 
        rob[i] only depends on leave[i-1]. leave[i] only depnds on rob[i-1] and leave[i-1].
        You can leave more than two houses in a row and not rob. We can use rolling array to save space. Just think about it. See below for code
        """
        # rob, leave = 0, 0
        # for v in nums:
        #     print(rob, leave)
        #     rob, leave = leave + v, max(rob, leave)
        # return max(rob, leave)

        # Solution 3:
        # prev1, prev2 = 0, 0
        # for num in nums:
        #     print("Before :", end="")
        #     print(prev1, prev2)
        #     prev1, prev2 = max(prev2 + num, prev1), prev1
        #     print("After :", end="")
        #     print(prev1, prev2)

        # return prev1

        # Solution 4: Faster and efficient and easy to understand
        """
        rob/leave decision at ith position, depends not maximum value gain between nums[i]+rob[i-2] and rob[i-1].
        if rob[i-1] is maximum, then we will leave ith position and put rob[i-1] gain as ith gain.
        if nums[i]+rob[i-2] is maximum, then we will choose to rob ith position.
        By this way we will acquire maximum gain at last house.
        """
        if not nums:
            return 0
        dp = [0]*len(nums)
        for i in range(len(nums)):
            if i < 1:
                dp[i] = nums[i]
            else:
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            print(dp)
        return dp[-1]


sol = Solution()
nums = [6, 3, 10, 8, 2, 10, 3, 5, 10, 5, 3]

print(sol.rob(nums))
"""
corner case:
1. money can be zero or positive
2. house can be less than 3; one house can be robbed, two adjacent house can not be robbed
[1], [1,1]
3. [1,3,1]
4. [2,1,1,2]
5.  [6, 3, 10, 8, 2, 10, 3, 5, 10, 5, 3]


"""
