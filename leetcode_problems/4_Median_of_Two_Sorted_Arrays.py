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
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        nums1_len = len(nums1)
        nums2_len = len(nums2)

        low = 0
        high = nums1_len

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (nums1_len + nums2_len + 1) // 2 - partitionX

            print(nums1[:partitionX], nums1[partitionX:])
            print(nums2[:partitionY], nums2[partitionY:])

            leftX_max = nums1[partitionX - 1] if partitionX else -float("Inf")
            rightX_min = nums1[partitionX] if partitionX < nums1_len else float("Inf")

            leftY_max = nums2[partitionY - 1] if partitionY else -float("Inf")
            rightY_min = nums2[partitionY] if partitionY < nums2_len else float("Inf")

            if leftX_max <= rightY_min and leftY_max <= rightX_min:
                if (nums1_len + nums2_len) % 2 == 0:
                    return (max(leftX_max, leftY_max) + min(rightX_min, rightY_min)) / 2

                else:

                    return max(leftX_max, leftY_max)

            elif leftX_max > rightY_min:
                # too far in the right

                high = partitionX - 1

            elif leftY_max > rightX_min:
                # too far in the left

                low = partitionX + 1

            


nums1 = [23, 26, 31, 35]
nums2 = [3, 5, 7, 9, 11, 16]
sol = Solution()
ans = sol.findMedianSortedArrays(nums1, nums2)
print(ans)
