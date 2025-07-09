"""
    Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:

Input: nums = [1,2,3], k = 0
Output: 0

Constraints:

    1 <= nums.length <= 3 * 104
    1 <= nums[i] <= 1000
    0 <= k <= 106
    
"""
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        # contiguous subarray
        ans = 0
        start = end = 0
        curr_product = 1
        while end < len(nums):
            curr_product = curr_product * nums[end]
            while start < len(nums) and curr_product >= k:
                curr_product = curr_product / nums[start]
                start += 1
            
            # if number of products less than k, then all individual will be less than k
            ans += end - start + 1
            end += 1
        
        return max(0, ans)

import unittest

class TestSuite(unittest.TestCase):
    
    def test_numSubarrayProductLessThanK(self):
        sol = Solution()
        nums = [10,5,2,6]
        k = 100
        self.assertEqual(
            sol.numSubarrayProductLessThanK(
                nums,
                k
            ),
            8
        )

if __name__ == "__main__":
    unittest.main()