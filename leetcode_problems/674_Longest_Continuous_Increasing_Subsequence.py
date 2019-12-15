"""
 Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:

Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 

Example 2:

Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 

"""


class Solution:
    def findLenthOfLCIS(self, nums):
        if len(nums) < 1:
            return 0
        local = nums[0]
        length = 1
        max_length = 1
        for i in range(1, len(nums)):
            if nums[i] > local:
                length += 1
                local = nums[i]
            else:
                local = nums[i]
                length = 1
            if length > max_length:
                max_length = length
        return max_length


sol = Solution()
nums = [-2, -3, 0, 3, 4]
print(sol.findLenthOfLCIS(nums))
"""
corner case:
1.no element []
2. one element [1]
"""
