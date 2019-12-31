"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Note:

    Each element in the result must be unique.
    The result can be in any order.

"""


class Solution:
    def intersection(self, nums1, nums2):
        # Solution 1: self, fastest
        # O(m+n)
        # return list(set(nums1).intersection(set(nums2)))

        # Solution 2: using &
        # O(m+n)

        # return set(nums1) & set(nums2)

        # Solution 3: not using built in function
        # O(m+n)
        # nums1 = set(nums1)
        # nums2 = set(nums2)
        # num = list(nums1) + list(nums2)
        # dic = {}
        # output = []
        # print(num)
        # for each in num:
        #     dic[each] = dic.get(each, 0) + 1
        #     if dic[each] > 1:
        #         output.append(each)
        # return output

        # Solution 4: using dictionary
        # O(m+n)
        output = []
        d = {}
        for each in nums1:
            d[each] = 1
        for each in nums2:
            if each in d and d[each] > 0:
                output.append(each)
                d[each] = 0
        return output


sol = Solution()
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(sol.intersection(nums1, nums2))

"""
converting a list to set requires O(n) time complexity
https://stackoverflow.com/questions/34642155/what-is-time-complexity-of-a-list-to-set-conversion/34642209
intersection
https://www.geeksforgeeks.org/intersection-function-python/
"""
