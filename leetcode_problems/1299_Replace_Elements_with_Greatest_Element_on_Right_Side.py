"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]

Constraints:

    1 <= arr.length <= 10^4
    1 <= arr[i] <= 10^5
"""


class Solution:
    def replaceElements(self, arr):
        # Solution 1: in-place change
        # time : O(n)
        # Space : O(1)
        curr_max = arr[-1]

        for i in range(len(arr) - 2, -1, -1):  # also take of duplicates
            val = arr[i]
            arr[i] = curr_max
            if val > curr_max:
                curr_max = val
        arr[-1] = -1
        return arr


sol = Solution()
arr = [17, 18, 5, 4, 6, 1]
print(sol.replaceElements(arr))


"""
clarifying questions:
1. duplicate elements?
"""
