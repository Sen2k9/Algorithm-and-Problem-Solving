"""
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].

Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""


class Solution:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        print(nums)
        half = len(nums[::2])

        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
        return nums

sol = Solution()
nums = [1, 5, 1, 1, 6, 4]
print(sol.wiggleSort(nums))

nums = [1, 3, 2, 2, 3, 1]
print(sol.wiggleSort(nums))

nums = [1,1,2,1,2,2,1]
print(sol.wiggleSort(nums))