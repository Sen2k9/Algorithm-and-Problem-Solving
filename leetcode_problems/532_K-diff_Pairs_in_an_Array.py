"""
 Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:

Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:

Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:

Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Note:

    The pairs (i, j) and (j, i) count as the same pair.
    The length of the array won't exceed 10,000.
    All the integers in the given input belong to the range: [-1e7, 1e7].

"""


class Solution:
    def findPairs(self, nums, k):
        # # Solution 1:
        # if len(nums) < 2 or k < 0:
        #     return 0
        # dic = {}
        # nums = sorted(nums) # to potentially find double match
        # dic[nums[0]] = 1
        # pairs = []
        # for i in range(1, len(nums)):
        #     val = nums[i]
        #     if (val + k) in dic:
        #         pairs.append((val, val + k))
        #     elif (val - k) in dic:
        #         pairs.append((val - k, val))
        #     dic[val] = 1
        #     print(val, pairs, nums)
        # if nums[-1] + k in dic and k != 0:
        #     pairs.append((nums[-1], nums[-1] + k))
        # if nums[-1] - k in dic and k != 0:
        #     pairs.append((nums[-1]-k, nums[-1]))
        # return len(set(pairs))
        # Solution 2:
        from collections import Counter
        if k < 0:
            return 0

        c = Counter(nums)  # Counter works as dictionary
        result = 0

        for num in c:
            if k != 0 and num + k in c or k == 0 and c[num] > 1:
                result += 1
        return result


sol = Solution()
nums = [2, 8, 6, 9, 7, 4, 9, 0, 5, 4]
k = 1
print(sol.findPairs(nums, k))
"""
corner case:
1. unique k-diff pairs: means there can be duplicate k-diff pairs which we need to eleminate
2. absulote difference :
3. negative, zero and positive values
4. array can be empty
5. k <= 0
6. val - k can have two candidate value
"""
