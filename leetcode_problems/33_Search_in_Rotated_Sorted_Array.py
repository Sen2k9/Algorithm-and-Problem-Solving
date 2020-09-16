"""
ou are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is guranteed to be rotated at some pivot.
-10^4 <= target <= 10^4
"""
class Solution:
    def search(self, nums, target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:

            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] >= nums[start]: # before pivot
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1

                else:
                    start = mid + 1


            else: # after pivot

                if target >= nums[mid] and target < nums[start]:
                    start = mid + 1

                else:
                    end = mid - 1


        return -1


sol = Solution()
nums = [4,5,6,7,0,1,2]; target = 0
print(sol.search(nums, target))

                

