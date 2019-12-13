"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6

Example 2:

Input: [1,2,3,4]
Output: 24

Note:

    The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
    Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

"""


class Solution:
    def maximumProduct(self, nums):
        nums = sorted(nums)
        pos_count = 0
        for each in nums:
            if each >= 0:
                pos_count += 1
        if pos_count == len(nums) or pos_count == 0:
            return nums[-1] * nums[-2] * nums[-3]
        elif pos_count == 1 or pos_count == 2:
            return nums[-1] * nums[0] * nums[1]
        elif pos_count >= 3:
            if nums[-1] * nums[-2]*nums[-3] > nums[0] * nums[1]*nums[-1]:
                return nums[-1] * nums[-2] * nums[-3]
            else:
                return nums[0]*nums[1]*nums[-1]


sol = Solution()
nums = [-100, -200, -1, 100]
print(sol.maximumProduct(nums))

"""
corner case:
1. all numbers are negative > [-1,-2,-3,-4]
2. only 2 positive and all are negative > [-200, -100, -1, 100, 200]
3. only 2 positive, Zero, and all are negative > [-1,-2,-3,-4, 0, 200,100]
4. Zero, and all are negative > [-1, -100, -2, 0]
5. one positive, all are negative > [-100, -200, -1, 100]
"""
