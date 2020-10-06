"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

    Return true if there exists i, j, k
    such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true

Example 2:

Input: [5,4,3,2,1]
Output: false

"""


class Solution:
    def increasingTriplet(self, nums) -> bool:
        # generalize solution
        # Time: O(n*k)
        # Space: O(k)
        k = 3  # number of incresing sequence we need
        seq_k = [float('Inf')] * (k - 1)
        for each in nums:
            for i in range(k-1):
                if each <= seq_k[i]:
                    seq_k[i] = each
                    break
            print(seq_k)
            if each > seq_k[-1]:
                return True
        return False


sol = Solution()
nums = [1,2,3,4,5]
print(sol.increasingTriplet(nums))

nums = [5,4,3,2,1]
print(sol.increasingTriplet(nums))

nums = [1,1,-2,6]
print(sol.increasingTriplet(nums))

nums = [1,1,1,1]
print(sol.increasingTriplet(nums))