"""
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.

Example 1:

Input: [2,1,2]
Output: 5

Example 2:

Input: [1,2,1]
Output: 0

Example 3:

Input: [3,2,3,4]
Output: 10

Example 4:

Input: [3,6,2,3]
Output: 8

Note:

    3 <= A.length <= 10000
    1 <= A[i] <= 10^6

"""


class Solution:
    def largestPerimeter(self, A):
        # Solution 1: self
        # A = sorted(A, reverse=True)
        # #print(A)

        # for i in range(len(A) - 2):
        #     if A[i] < A[i + 1] + A[i + 2]:
        #         # if 2 smaller sides are bigger than the biggest
        #         return A[i] + A[i + 1] + A[i + 2]
                
        # return 0

        # Solution 2: faster
        A = sorted(A, reverse=True)
        #print(A)
        i = 0
        while i < len(A) - 2:
            if A[i] < A[i + 1] + A[i + 2]:
                    # if 2 smaller sides are bigger than the biggest
                return A[i] + A[i + 1] + A[i + 2]
            i+=1
                
        return 0


sol = Solution()
A = [2,1,2]
print(sol.largestPerimeter(A))

"""
perimeter = A+B+C
inequality : a+b > c
"""
