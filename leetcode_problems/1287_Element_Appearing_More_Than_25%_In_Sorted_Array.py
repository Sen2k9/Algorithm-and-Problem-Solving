"""
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

 

Constraints:

    1 <= arr.length <= 10^4
    0 <= arr[i] <= 10^5

"""


class Solution:
    def findSpecialInteger(self, arr):
        dic = {}
        if len(arr) == 1:
            return arr[0]
        for each in arr:
            if each not in dic:
                dic[each] = 1
            else:
                dic[each] += 1
                if dic[each] > len(arr) // 4:
                    return each


sol = Solution()
arr = [1, 2, 2, 6, 6, 6, 6, 7, 10, 10, 11, 12, 13]
print(sol.findSpecialInteger(arr))
"""
corner case:
1. length of array is 1
"""
