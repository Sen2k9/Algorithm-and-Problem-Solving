"""
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.
Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.

Constraints:

    1 <= arr1.length, arr2.length, arr3.length <= 1000
    1 <= arr1[i], arr2[i], arr3[i] <= 2000
"""


class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        # Solution 1:
        # time : O(n)
        # space : O(n)
        dictionary = {}
        for i in range(len(arr1)):
            dictionary[arr1[i]] = dictionary.get(arr1[i], 0) + 1
            dictionary[arr2[i]] = dictionary.get(arr2[i], 0) + 1
            dictionary[arr3[i]] = dictionary.get(arr3[i], 0) + 1
        result = []
        # print(dictionary)

        for key, val in dictionary.items():
            if val == 3:
                result.append(key)
        return sorted(result)


sol = Solution()
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]
print(sol.arraysIntersection(arr1, arr2, arr3))
