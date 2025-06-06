"""
    
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

 

Constraints:

    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105


"""
from typing import List
import unittest

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort() # nlogn
        result = []
        # O(n^2)
        for idx, val in enumerate(nums):

            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            
            left_ptr = idx + 1
            right_ptr = len(nums) - 1

            while left_ptr < right_ptr:
                threesum = nums[idx] + nums[left_ptr] + nums[right_ptr]

                if threesum > 0:
                    right_ptr -= 1
                elif threesum < 0:
                    left_ptr += 1
                
                else:
                    result.append(
                        [nums[idx], nums[left_ptr], nums[right_ptr]]
                    )
                    left_ptr += 1
                    # move the left pointer
                    while left_ptr < right_ptr and nums[left_ptr] == nums[left_ptr - 1]:
                        left_ptr += 1 # increment to next val
        
        return result
    
class TestSuite(unittest.TestCase):
    
    def test_3sum(self):
        sol = Solution()
        
        nums = [-1,0,1,2,-1,-4]
        output = [[-1,-1,2],[-1,0,1]]
        self.assertEqual(
            sol.threeSum(nums),
            output
        )
        
        nums = [0,1,1]
        output = []
        self.assertEqual(
            sol.threeSum(nums),
            output
        )

if __name__ == "__main__":
    unittest.main()