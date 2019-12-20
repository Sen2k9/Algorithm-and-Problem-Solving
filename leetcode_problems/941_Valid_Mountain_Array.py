"""
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

    A.length >= 3
    There exists some i with 0 < i < A.length - 1 such that:
        A[0] < A[1] < ... A[i-1] < A[i]
        A[i] > A[i+1] > ... > A[A.length - 1]
Note:

    0 <= A.length <= 10000
    0 <= A[i] <= 10000 


"""


import pdb


class Solution:
    def validMountainArray(self, A):
        if len(A) < 3:
            return False
        mid = A.index(max(A))
        l = A[:mid]
        r = A[mid:]
        left = set(l)
        right = set(r)
        if len(left) != len(l) or len(right) != len(r) or len(l) < 1 or len(r) == 1:
            return False

        prev = A[mid]
        for i in range(len(l)-1, -1, -1):
            if prev - l[i] <= 0:
                return False
            prev = l[i]
        prev = A[mid]
        for i in range(1, len(r)):
            if prev - r[i] <= 0:
                return False
            prev = r[i]
        return True


sol = Solution()
A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# pdb.set_trace()
print(sol.validMountainArray(A))
"""
corner case:
1. lenght > 3
2. continguous duplicate elements
3. max value is at the biggining or end
"""
