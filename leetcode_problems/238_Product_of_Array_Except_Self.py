"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""


class Solution:
    def productExceptSelf(self, nums):
        # time : O(n)
        # space : O(1)
        output = []
        for i in range(len(nums)):
            if i > 0:
                output.append(output[-1] * nums[i])
            else:
                output.append(nums[i])
        right_product = None
        i = len(nums) - 1
        while i >= 0:
            right_product = right_product * \
                nums[i+1] if right_product != None else 1
            output[i] = right_product*output[i - 1] if i - \
                1 >= 0 else right_product
            i -= 1
        return output


sol = Solution()
nums = [0, 0]

print(sol.productExceptSelf(nums))
"""
https://leetcode.com/problems/product-of-array-except-self/discuss/489326/Python-Solution-%2B-Thought-Process.-O(1)-space-O(n)-time
"""
