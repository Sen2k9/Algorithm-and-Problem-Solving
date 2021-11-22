import heapq


class Solution:
    
    def find_k_largest_numbers(self, nums, k):
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap

import unittest


class TestSolution(unittest.TestCase):

    def test_k_largest_numbers(self):
        sol = Solution()
        ans = sol.find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)
        self.assertTrue(ans)
        print("Here are the top K numbers: " +
        str(sol.find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

        ans = sol.find_k_largest_numbers([5, 12, 11, -1, 12], 3)
        self.assertTrue(ans)
        print("Here are the top K numbers: " +
        str(sol.find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


if __name__ == '__main__':
    unittest.main()
