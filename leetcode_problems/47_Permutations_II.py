"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution:
    def permuteUnique(self, nums):
        # if len(nums) < 2:
        #     return nums
        nums.sort()

        return self.backtrack(nums)

        # return self.ans

    def backtrack(self, nums):
        if len(nums) == 1:
            return [nums]

        temp = []
        prev = float("Inf")
        for i in range(len(nums)):
            res = nums[i]
            if res == prev:
                continue
            prev = res

            rest = nums[:i] + nums[i + 1:]
            # print(rest)

            for each in self.backtrack(rest):
                # print(each)
                temp.append([res] + each)

        # print(temp)
        return temp


sol = Solution()
nums = [1]
print(sol.permuteUnique(nums))
