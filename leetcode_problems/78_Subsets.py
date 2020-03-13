"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution:
    def subsets(self, nums):
        # time : O(2**n)
        # Space : O(2**n)

        # upper_bound = 2 ** len(nums)
        # ans = []

        # for decimal_val in range(upper_bound):
        #     inner_loop = []
        #     for bit in range(len(nums)):
        #         if decimal_val & (1 << bit) != 0:
        #             inner_loop.append(nums[bit])

        #     ans.append(inner_loop)
        # return ans

        # Solution 2:

        # ans = [[]]

        # for each in nums:

        #     ans = ans + [element + [each] for element in ans]
        #     # print(ans)

        # return ans

        # Solution 3:
        from itertools import combinations

        ans = []
        for i in range(len(nums) + 1):
            ans = ans + [list(comb) for comb in combinations(nums, i)]

        return ans


sol = Solution()
nums = [1, 2, 3, 4]
print(sol.subsets(nums))
"""
references:
https://leetcode.com/problems/subsets/discuss/527606/Several-python-solution-w-Explanation-and-Demo
"""
