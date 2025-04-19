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
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find pivot, as smallest element from right boundary

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            # that means smallest element is on the right side
            if nums[mid] > nums[-1]:
                left = mid + 1
            # either it is the pivot or in the left side
            # if right go beyond the boundary then the left value is the pivot
            else:
                right = mid - 1
        
        pivot = left

        def binary_search(left_boundary, right_boundary, target):

            while left_boundary <= right_boundary:
                mid = left_boundary + (right_boundary - left_boundary) // 2

                if nums[mid] == target:
                    return mid
                
                elif nums[mid] > target:
                    right_boundary = mid - 1
                
                else:
                    left_boundary = mid + 1
            
            # otherwise not found
            return - 1
        
        # find target either in left side of pivot or right side
        left_search = binary_search(0, left - 1, target)
        right_search = binary_search(left, len(nums) - 1, target)

        if left_search != -1:
            return left_search
        
        return right_search



