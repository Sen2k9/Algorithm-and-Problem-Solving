"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3

Example 2:

Input: [3,4,-1,1]
Output: 2

Example 3:

Input: [7,8,9,11,12]
Output: 1

"""


class Solution:
    def firstMissingPositive(self, nums) -> int:
        # Best Solution: Time O(n), Space O(1)
        # if len(nums) == 1:
        #     if nums[0] == 1:
        #         return 2
        #     else:
        #         return 1
        
        # if 1 not in nums:
        #     return 1
        # n = len(nums)
        
        # for i, val in enumerate(nums):
        #     if val < 1 or val > n:
        #         nums[i] = 1

        # print(nums)
        # for i, val in enumerate(nums):
        #     a = abs(nums[i])

        #     if a == n:
        #         nums[0] = - abs(nums[0])

        #     else:
        #         nums[a] = - abs(nums[a])

        # print(nums)

        # for i in range(1, n):
        #     if nums[i] > 0:
        #         return i

        # if nums[0] > 0:
        #     return n

        # return n + 1
        
        # Time: O(n), Space: O(n)

        result = [0] * (len(nums) + 1)

        for i, val in enumerate(nums):
            if val > 0 and val <= len(nums):
                result[val] = val

        for i in range(1, len(result)):
            if result[i] != i:
                return i
        return len(nums) + 1



        

sol = Solution()
nums = [7,3,5,11,12, 1]
print(sol.firstMissingPositive(nums))

nums = [1, 2, 3, 4, 5, 6]
print(sol.firstMissingPositive(nums))

nums = [1,2,0]
print(sol.firstMissingPositive(nums))

nums = [1]
print(sol.firstMissingPositive(nums))

nums = [2]
print(sol.firstMissingPositive(nums))