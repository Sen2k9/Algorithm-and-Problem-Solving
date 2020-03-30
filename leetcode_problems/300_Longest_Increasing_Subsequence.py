"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:

    There may be more than one LIS combination, it is only necessary for you to return the length.
    Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""


class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = [1] * len(nums)
        max_length = 1

        for i in range(len(nums)):
            for j in range(0, i + 1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
                    if dp[i] > max_length:
                        max_length = dp[i]
        # print(dp)
        return max_length


sol = Solution()
n = [0]


print(sol.lengthOfLIS(n))
"""
[1,3,6,7,9,4,10,5,6]

"""
