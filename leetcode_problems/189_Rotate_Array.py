"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:

    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?

"""


class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        # if len(nums) < 2:
        #     return nums
        # for i in range(k):
        #     b = nums.pop(len(nums)-1)
        #     nums.insert(0, b)

        # return nums
        # Solution 2: More efficient
        k = k % len(nums)
        # print(id(nums))
        nums[:] = nums[-k:] + nums[:-k]
        # print(id(nums))
        return nums


sol = Solution()
nums = [-1, -100, 3, 99]
k = 2
print(sol.rotate(nums, k))
"""
corner case:
1. make sure your array/list object type and id is same
"""
