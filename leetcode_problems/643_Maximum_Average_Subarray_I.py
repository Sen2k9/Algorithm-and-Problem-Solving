"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75



Note:

    1 <= k <= n <= 30,000.
    Elements of the given array will be in the range [-10,000, 10,000].

"""


class Solution:
    def findMaxAverage(self, nums, k):
        # Solution 1: brute-force, not efficient
        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        # dp = []
        # i = k - 1
        # j = 0

        # while i < n:
        #     local = 0
        #     for a, val in enumerate(nums[j: i + 1]):
        #         local = local + val
        #     dp.append(local / k)
        #     print(local, dp)
        #     i += 1
        #     j += 1
        # return max(dp)
        # Solution 2: medium efficient
        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        # i = k - 1
        # j = 0
        # max_value = 0
        # for each in range(j, i + 1):
        #     max_value += nums[each]
        # i = i + 1
        # prev = max_value
        # local = 0
        # while i < n:
        #     print(prev)
        #     local = prev - nums[j]
        #     if (local+nums[i]) > max_value:
        #         max_value = local + nums[i]
        #     prev = local + nums[i]

        #     i += 1
        #     j += 1
        # return max_value/k
        # Solution 3: efficient, using enumerate
        # max_value = current = sum(nums[0:k])
        # for i, val in enumerate(nums[k:], start=0):
        #     print(i, val)
        #     current = current + val - nums[i]
        #     if current > max_value:
        #         max_value = current
        # return max_value / k
        # Solution 4: more efficient, two window method
        common = sum(nums[0:k])  # first window
        M = d = 0
        for i, val in enumerate(nums[k:], start=0):
            d += val - nums[i]
            print(d)
            if d > M:
                M = d  # second window
        return (common+M)/k


sol = Solution()
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(sol.findMaxAverage(nums, k))
"""
corner case:
1. k = n =1
2. [0, 4, 0, 3, 2]
3. k =1
"""
