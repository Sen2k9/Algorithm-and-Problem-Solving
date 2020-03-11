"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""


class Solution:
    def topKFrequent(self, nums, k: int):
        # Solution 1: brute-force,
        # time : O(nlogn)
        # Space : O(n)
        # count_by_key = {}
        # for each in nums:
        #     if each in count_by_key:
        #         count_by_key[each] += 1
        #     else:
        #         count_by_key[each] = 1
        # print(count_by_key)
        # sorted_keys = sorted(count_by_key.items(),
        #                      key=lambda x: x[1], reverse=True)

        # ans = []
        # print(sorted_keys)

        # for i in range(k):
        #     ans.append(sorted_keys[i][0])
        # return ans

        # Solution 2: using heapq
        # time : O(nlogk)
        # Space : O(n)

        import heapq

        freq_by_key = {}

        for each in nums:
            if each in freq_by_key:
                freq_by_key[each] += 1
            else:
                freq_by_key[each] = 1
        h = []

        for key in freq_by_key:
            heapq.heappush(h, (freq_by_key[key], key))
            #print(h, len(h), k)
            if len(h) > k:
                heapq.heappop(h)

        ans = []
        print(h)
        while h:  # O(logk)
            _, item = heapq.heappop(h)
            ans.append(item)
        return ans


sol = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2


#k = 2
print(sol.topKFrequent(nums, k))

"""
corner case:
1. integer <= [+/-]digit{digit}

reference:
https://leetcode.com/problems/top-k-frequent-elements/discuss/484980/Python-Explained-Two-Simple-Heap-solutions
"""
