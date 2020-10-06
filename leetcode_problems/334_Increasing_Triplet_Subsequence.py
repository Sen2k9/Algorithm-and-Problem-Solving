"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

    Return true if there exists i, j, k
    such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true

Example 2:

Input: [5,4,3,2,1]
Output: false

"""


class Solution:
    def increasingTriplet(self, nums) -> bool:
        dp = [0] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    temp = dp[j] + 1
                    dp[i] = max(dp[i], temp)

                if dp[i] >= 3:
                    return True
                
                print(dp, i, j, nums[i], nums[j])




sol = Solution()
nums = [1,2,3,4,5]
print(sol.increasingTriplet(nums))