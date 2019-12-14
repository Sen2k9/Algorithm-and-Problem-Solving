"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]

Follow up:

Could you optimize your algorithm to use only O(k) extra space?

"""


class Solution:
    def getRow(self, rowIndex):
        # Solution 1:
        # keeping the whole array 0>k rows and then output k rows
        # k = rowIndex
        # arr = [[1]]
        # if k < 1:
        #     return arr[0]
        # else:
        #     for i in range(1, k + 1):
        #         temp = [1] * (i + 1)
        #         for j in range(1, i):
        #             temp[j] = arr[i - 1][j - 1] + arr[i - 1][j]
        #         arr.append(temp)
        # return arr[k]

        # Solution 2:
        # better solution: not storing memorry from 0 to k rows
        k = rowIndex
        output = []
        if k == 0:
            return [1]
        elif k == 1:
            return [1, 1]

        else:
            l = [1, 1]

            for i in range(2, k + 1):
                prevRow = l
                j = 1
                l = [1, 1]
                n = len(prevRow)
                while j < n:
                    value = prevRow[j] + prevRow[j - 1]

                    l.insert(j, value)
                    j += 1
                output = l
                # print(output)
            return output


sol = Solution()
n = 31
print(sol.getRow(n))

"""
[
    [1]
    [1,1]
    [1,2,1]
    [1,3,3,1]
    [1,4,6,4,1]
]
corner case:
1. non negative integer: 0,1,2
"""
