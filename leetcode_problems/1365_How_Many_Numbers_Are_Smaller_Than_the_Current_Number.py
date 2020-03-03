"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

 

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]

Constraints:

    2 <= nums.length <= 500
    0 <= nums[i] <= 100
"""


class Solution:
    def smallerNumbersThanCurrent(self, nums):
        # Solution 1:
        # Time : O(nlogn)
        # Space : O(n)
        dic = {}
        for each in nums:
            if each not in dic:
                dic[each] = 1
            else:
                dic[each] += 1
        sorted_list = sorted(list(set(nums)), reverse=True)
        #print(s, dic)

        smaller_mapping = {}
        total_count = len(nums)

        upto = 0
        for each in sorted_list:
            smaller_mapping[each] = total_count - upto - dic[each]
            upto = upto + dic[each]
        # print(smaller_mapping)

        return [smaller_mapping[i] for i in nums]


sol = Solution()
nums = [7, 7]
print(sol.smallerNumbersThanCurrent(nums))
