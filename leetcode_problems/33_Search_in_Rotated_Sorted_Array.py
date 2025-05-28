"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

[4,5,6,7,   0,1,2] target = 0
l2     r2   l1  r1
Conditions:
if mid > target and target < r1 and mid < r1:
    search left

if mid > target and target > l2 and mid > l2:
    search left

if mid < target and target > l2 and mid > l2:
    search right

if mid < target and target < r1 and mid < r1:
    search right

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1

 

Constraints:

    1 <= nums.length <= 5000
    -104 <= nums[i] <= 104
    All values of nums are unique.
    nums is an ascending array that is possibly rotated.
    -104 <= target <= 104


"""
import unittest
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def find_pivot(nums):
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] > nums[-1]: # compare with respect to last element
                    left = mid + 1 # search right
                
                else:
                    right = mid - 1 # search left
            
            return left

        pivot = find_pivot(nums)
        #print(pivot)

        def binary_search(arr, target):

            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] == target:
                    return mid
                
                elif arr[mid] > target:
                    right = mid - 1
                
                else:
                    left = mid + 1
            
            return -1

        # search left of pivot
        result = binary_search(nums[:pivot], target)
        if result > -1:
            return result
        
        # search right of pivot
        result = binary_search(nums[pivot:], target)
        if result > -1:
            return result + pivot
        
        return - 1


class TestSuite(unittest.TestCase):
    
    def test_search(self):
        sol = Solution()
        nums = [4,5,6,7,0,1,2]
        target = 3
        
        self.assertEqual(
            sol.search(nums, target),
            -1
        )

if __name__ == "__main__":
    unittest.main()
        

