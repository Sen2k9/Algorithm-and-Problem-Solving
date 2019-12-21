"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:

Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Note:

    Then length of the input array is in range [1, 10,000].
    The input array may contain duplicates, so ascending order here means <=.

"""


class Solution:
    def findUnsortedSubarray(self, nums):
        # Solution 1: best solution
        arr = sorted(nums)
        print(arr)
        start = -1
        end = -1
        i = 0
        while i < len(nums):
            if nums[i] != arr[i]:
                start = i
                break
            i += 1
        if start == -1:
            return 0  # already
        i = len(nums) - 1
        while i > 0:
            if nums[i] != arr[i]:
                end = i
                break
            i -= 1
        return (end-start)+1


sol = Solution()
nums = [2, 3, 3, 2, 4]
print(sol.findUnsortedSubarray(nums))
"""
corner case:
1. [1, 3, 2, 2, 2]
2. [2,3,3,2,4]
"""
