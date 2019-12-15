"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""


class Solution:
    def maxSubArray(self, nums):
        # Solution 1: Dynamic Programming
        if (nums is None):
            return 0
        elif(len(nums) == 1):
            return nums[0]
        elif(max(nums) < 0):
            return(max(nums))
        else:
            global_max = nums[0]
            dp = [0] * (len(nums))
            dp[0] = nums[0]
            for i in range(1, len(nums)):
                dp[i] = max(nums[i], dp[i-1] + nums[i])
                #print(dp, global_max)
                if dp[i] > global_max:
                    global_max = dp[i]
            return global_max
        # # Solution 2: greedy approach
        # max_sum = nums[0]
        # local_sum = nums[0]
        # for i in range(1, len(nums)):
        #     if local_sum < 0:
        #         local_sum = nums[i]
        #     else:
        #         local_sum = local_sum + nums[i]
        #     if local_sum > max_sum:
        #         max_sum = local_sum
        # return max_sum


sol = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(sol.maxSubArray(nums))
"""
corner case:
1. all negative number
2. only one number
"""
