"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:

    You may assume that the array does not change.
    There are many calls to sumRange function.

"""


class NumArray:
    # Solution 1: self, Runtime: 99.89%

    def __init__(self, nums):
        self.nums = nums
        # using dictionary can also increase runtime efficiency, instead of creating a list and then assigning values
        self.dp = [0] * len(nums)
        for i in range(len(self.nums)):
            self.dp[i] = self.dp[i - 1] + self.nums[i]
        #print(self.dp, sum(nums))

    def sumRange(self, i: int, j: int):
        if i == 0:
            return self.dp[j]
        return self.dp[j]-self.dp[i-1]


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
param_1 = obj.sumRange(0, 2)
print(param_1)
"""
corner case:
1. this problem requires no iteration in sumRange function
"""
