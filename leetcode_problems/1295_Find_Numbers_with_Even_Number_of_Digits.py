"""
Given an array nums of integers, return how many of them contain an even number of digits.
Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.

Constraints:

    1 <= nums.length <= 500
    1 <= nums[i] <= 10^5
"""


class Solution:
    def findNumbers(self, nums):
        # Solution 1:
        # Time : O(n)
        # space : O(1)
        import math
        count = 0
        for each in nums:
            if (int(math.log(each, 10)) + 1) % 2 == 0:  # not sure with the complexity of math.log
                count += 1
        return count
        # Solution 2:
        # nums_str = [str(each) for each in nums]  # O(n)
        # len_nums = [len(each) for each in nums_str]  # O(n)
        # count = 0
        # for each in len_nums:
        #     if each % 2 == 0:
        #         count += 1
        # return count
        # Solution 3:
        # Time :O(nlogn)
        # Space : O(1)
        # result = 0

        # for each in nums:  # O(nlog10(n))
        #     digits = 0

        #     while each > 0:  # log10(each)
        #         each = each // 10
        #         digits += 1
        #     if digits % 2 == 0:
        #         result += 1
        # return result


sol = Solution()
nums = [555, 901, 482, 1771]
print(sol.findNumbers(nums))
