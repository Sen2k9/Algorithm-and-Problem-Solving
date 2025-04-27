"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

 

Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

 

Constraints:

    nums.length will be between 1 and 50,000.
    nums[i] will be an integer between 0 and 49,999.

"""
from typing import List
import unittest

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = 0
        answer = len(nums)

        freq = {}
        first_seen = {}
        for idx, val in enumerate(nums):
            if val not in first_seen:
                first_seen[val] = idx
            
            freq[val] = freq.get(val, 0) + 1

            if freq[val] > degree:
                degree = max(degree, freq[val])
                answer = idx - first_seen[val] + 1
            
            # if their another number with same degree, calculate for that too
            elif freq[val] == degree:
                # find minimum of the same degree number
                answer = min(answer, idx - first_seen[val] + 1)
        
        return answer
    
class TestSuite(unittest.TestCase):
    
    def test_degree_of_an_array(self):
        # call the solution class
        sol = Solution()
        # first test
        nums = [1,2,2,3,1]
        # find match
        self.assertEqual(
            sol.findShortestSubArray(nums),
            2
        )
        # second test
        nums = [1,2,2,3,1,4,2]
        self.assertEqual(
            sol.findShortestSubArray(nums),
            6
        )

if __name__ == "__main__":
    unittest.main()