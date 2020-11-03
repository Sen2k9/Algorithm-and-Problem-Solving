"""
Given an array of integers and an integer k, 
you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

Constraints:

    The length of the array is in range [1, 20,000].
    The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

"""
from collections import defaultdict


class Solution:
    def subarraySum(self, nums, k: int) -> int:
        map_sum = defaultdict(int)
        count = 0
        map_sum[0] = 1

        local_sum = 0

        for num in nums:
            local_sum += num
            if local_sum - k in map_sum:
                count += map_sum[local_sum - k]

            map_sum[local_sum] += 1

            print(map_sum, count)
        return count

sol = Solution()
nums = [3, -1, 0, 1, 1, 1, 2]
k = 2
print(sol.subarraySum(nums, k))
nums = [0,0,0,0,0,0,0,0,0,0]
k = 0
print(sol.subarraySum(nums, k))

nums = [-1,-1,1]
k = 1
print(sol.subarraySum(nums, k))

nums = [1,1,1]
k = 2
print(sol.subarraySum(nums, k))

nums = [-1,-1,1]
k = 0
print(sol.subarraySum(nums, k))

nums = [3, -1, 0, 1, 1, 1, 2]
k = 2
print(sol.subarraySum(nums, k))
