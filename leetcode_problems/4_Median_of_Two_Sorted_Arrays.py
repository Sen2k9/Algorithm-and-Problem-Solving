"""
Given two sorted arrays nums1 and nums2 of size m and n respectively.

Return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000

 

Constraints:

    nums1,length == m
    nums2,length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000


"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        index1 = 0
        index2 = 0
        merged_list = []

        while index1 < len(nums1) and index2 < len(nums2):

            if nums1[index1] <= nums2[index2]:
                merged_list.append(nums1[index1])
                index1 += 1
            
            else:
                merged_list.append(nums2[index2])
                index2 += 1
            
        while index1 < len(nums1):
            merged_list += nums1[index1:]
            index1 = len(nums1)

        while index2 < len(nums2):
            merged_list += nums2[index2:]
            index2 = len(nums2)
        
        ans = 0
        if len(merged_list) % 2 == 0:
            ans = (merged_list[len(merged_list)//2] + 
                   merged_list[len(merged_list)//2 - 1]) / 2

        else:

            ans = merged_list[len(merged_list)//2]

        return ans


nums1 = [1, 3]
nums2 = [2]
sol = Solution()
ans = sol.findMedianSortedArrays(nums1, nums2)
print(ans)
