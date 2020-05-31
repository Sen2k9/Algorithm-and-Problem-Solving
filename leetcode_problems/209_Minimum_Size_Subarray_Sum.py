"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

"""


class Solution:
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0

        forward = 0
        backward = 0
        total = 0
        ans = float('inf')

        while forward < len(nums):

            total += nums[forward]

            while total >= s:
                if forward - backward + 1 < ans:
                    ans = forward - backward + 1

                total = total - nums[backward]

                backward += 1

            forward += 1

        if ans == float('inf'):
            return 0
        else:
            return ans


sol = Solution()
s = 7
nums = [2, 3, 1, 2, 4, 3]
print(sol.minSubArrayLen(s, nums))

"""
runtime : 2n > O(n)
"""
