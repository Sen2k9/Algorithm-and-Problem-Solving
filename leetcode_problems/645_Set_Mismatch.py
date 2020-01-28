"""
 The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]

Note:

    The given array size will in the range [2, 10000].
    The given array's numbers won't have any order.

"""


class Solution:
    def findErrorNums(self, nums):
        # Solution 1: self
        # dic = {}
        # for i in range(1, len(nums) + 1):
        #     dic[i] = 1
        # from collections import Counter
        # original = Counter(nums)
        # res = []

        # for each in dic:
        #     if each not in original:
        #         res.append(each)
        #     elif original[each] == 2:
        #         res.insert(0, each)
        # return res

        # Solution 2: faster
        # from collections import Counter
        # dic = Counter(nums)
        # res = []

        # for i in range(1, len(nums) + 1):
        #     if dic[i] == 2:
        #         res.insert(0, i)
        #     elif i not in dic:
        #         res.append(i)
        # return res

        # Solution 3: not using dictionary, fastest

        # n = len(nums)
        # total = n*(n + 1) // 2
        # miss = total - sum(set(nums))

        # duplicate = sum(nums) - sum(set(nums))
        # return [duplicate, miss]

        # Solution 4: fastest
        n = [-1] * len(nums)
        res = []
        for i in nums:
            if n[i - 1] != -1:
                res.append(i)
            n[i - 1] = 1

        return res + [n.index(-1)+1]


sol = Solution()
nums = [2, 1, 2]
print(sol.findErrorNums(nums))
