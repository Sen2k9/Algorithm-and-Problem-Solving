"""
We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:

Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.

"""


class Solution:
    def findLHS(self, nums):
        # solution 1:
        # if len(nums) <= 1:
        #     return 0
        # from collections import Counter
        # dic = Counter(nums)

        # longest = 0
        # for each in nums:
        #     if each - 1 in dic and dic[each] + dic[each - 1] > longest:
        #         longest = dic[each] + dic[each - 1]

        # return longest

        # Solution 2: fastest

        from collections import Counter
        dic = Counter(nums)
        longest = 0

        for k in dic:

            if k + 1 in dic and dic[k] + dic[k + 1] > longest:

                longest = dic[k] + dic[k + 1]
        return longest


sol = Solution()
nums = [1, 2, 3, 3, 1, -14, 13, 4]

print(sol.findLHS(nums))

"""
corner case:
[1,1,1,1]
[1,3,5,7,9,11,13,15,17]
[1, 2, 3, 3, 1, -14, 13, 4]
"""
