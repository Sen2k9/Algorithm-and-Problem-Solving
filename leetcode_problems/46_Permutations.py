"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:
    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        result = []
        for i in range(len(nums)):
            choose_one = nums[i]

            remList = nums[:i] + nums[i + 1:]
            for m in self.permute(remList):
                result.append([choose_one]+m)
            # print(result)

        return result


sol = Solution()
nums = [1, 2, 3]
print(sol.permute(nums))
"""
https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/
"""
