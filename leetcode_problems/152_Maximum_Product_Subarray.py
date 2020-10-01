"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""


class Solution:
    def maxProduct(self, nums) -> int:
        
        # greedy/ dynamic programming
        if not nums:
            return 0
        max_so_far = min_so_far = result = nums[0]

        for i in range(1, len(nums)):

            current = nums[i]

            temp_max = max(current * min_so_far, current * max_so_far, current)

            min_so_far = min(current * min_so_far, current * max_so_far, current)

            max_so_far = temp_max

            result = max(result, max_so_far)

            print(max_so_far, min_so_far, result)

        return result

            



sol = Solution()

nums = [2, -5, 3, 1, -4, 0, -10, 2, 8]
print(sol.maxProduct(nums))

# nums = [2,3,-2,4]
# print(sol.maxProduct(nums))

# nums = [5, -4, 3, -2, -1]
# print(sol.maxProduct(nums))

# nums = [-2,0,-1]
# print(sol.maxProduct(nums))

# nums = [0,2]
# print(sol.maxProduct(nums))