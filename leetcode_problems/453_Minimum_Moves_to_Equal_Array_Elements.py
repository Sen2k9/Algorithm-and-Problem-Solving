"""
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""


class Solution:
    def minMoves(self, nums):
        # Soution 1:
        m = min(nums)

        total = 0
        for each in nums:
            total += (each - m)
        return total

        # Solution 2: faster
        t = sum(nums)
        n = len(nums)
        m = min(nums)
        return t-n*m


sol = Solution()
nums = [2, 5, 7]
print(sol.minMoves(nums))
