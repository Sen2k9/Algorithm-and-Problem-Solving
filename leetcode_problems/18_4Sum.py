"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]


"""


class Solution:
    def fourSum(self, nums, target: int):

        nums.sort()
        ans = []

        print(nums)

        # if nums[0] * 4 > target or nums[-1] * 4 < target:
        #     return ans
        for i in range(len(nums)-3):

            for j in range(i+1, len(nums) - 2):

                new_target = target - nums[i] - nums[j]

                start = j + 1

                end = len(nums) - 1
                while start < end:

                    if nums[start] + nums[end] == new_target:
                        temp = []
                        temp.append(nums[i])
                        temp.append(nums[j])
                        temp.append(nums[start])
                        temp.append(nums[end])

                        if temp not in ans:
                            ans.append(temp)

                        start += 1
                        end -= 1

                        while start < end and nums[start - 1] == nums[start]:
                            start += 1

                        while start < end and nums[end] == nums[end + 1]:

                            end -= 1

                    elif (nums[start] + nums[end]) < new_target:
                        start += 1

                    elif (nums[start] + nums[end]) > new_target:
                        end -= 1

                    #print(start, end)

        return ans

sol = Solution()
nums = [1,-2,-5,-4,-3,3,3,5]
target = -11
print(sol.fourSum(nums, target))
