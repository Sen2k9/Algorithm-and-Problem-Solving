"""
 Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:

Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:

Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.

Note: The n belongs to [1, 10,000]. 
"""


class Solution:
    def checkPossibility(self, nums):
        if len(nums) < 2:
            return True
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if count > 0:
                    return False
                else:
                    count += 1
                    if i == 0:
                        pass
                    elif nums[i - 1] >= nums[i + 1]:
                        nums[i+1] = nums[i]

        return count <= 1


sol = Solution()
nums = [2, 3, 3, 2, 4]

print(sol.checkPossibility(nums))
"""
corner case:
1. array length 1 > [1]
2. array is already sorted > [1,2,3]
3. different lower value > [4,3,2,3]
4. [2, 3, 3, 2, 4]
"""
