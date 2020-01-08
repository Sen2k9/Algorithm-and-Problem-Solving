"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4

"""


class Solution:
    def singleNumber(self, nums):
        # Solution 1: self, using dictionary
        # O(n), extra space O(n)
        # dic = {}
        # for each in nums:
        #     dic[each] = dic.get(each, 0) + 1
        # for k, v in dic.items():
        #     if v == 1:
        #         return k

        # Solution 2: bit manipulation
        # O(n), O(1) memory
        result = 0
        for each in nums:
            result = result ^ each
        return result

        # Solution 3: using set
        # res = set()

        # for each in nums:
        #     if each in res:
        #         res.remove(each)
        #     else:
        #         res.add(each)
        # return res.pop()


sol = Solution()
nums = [4, 1, 2, 1, 2]
print(sol.singleNumber(nums))
"""
reference:
https://leetcode.com/problems/single-number/discuss/468420/Python3-Bitwise-and-Non-Bitwise-Solutions-(w-Explanation)
"""
