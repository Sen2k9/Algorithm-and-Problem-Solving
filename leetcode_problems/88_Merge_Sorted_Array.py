"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = 0
        i = 0
        j = 0
        arr1 = nums1[0:m]
        while i < m and j < n:
            if arr1[i] < nums2[j]:
                nums1[k] = arr1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1

            k += 1
        while i < m:
            nums1[k] = arr1[i]
            i += 1
            k += 1
        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1
        return nums1


sol = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(sol.merge(nums1, m, nums2, n))
"""
corner case:
1. in-place changing of nums1

"""
