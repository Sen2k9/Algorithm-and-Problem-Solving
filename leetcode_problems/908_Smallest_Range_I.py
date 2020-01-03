"""
Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.

Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]

Example 2:

Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]

Example 3:

Input:  A= [1,3,6], K = 3
Output: 0
Explanation: B = [3,3,3] or B = [4,4,4]

Note:

    1 <= A.length <= 10000
    0 <= A[i] <= 10000
    0 <= K <= 10000

"""


class Solution:
    def smallestRangeI(self, A, K):
        # Solution 1: faster
        # O(n)
        a = min(A)  # O(n)
        b = max(A)  # O(n)
        diff = b - a
        if diff <= (2 * K):
            return 0
        else:
            return (diff - (2 * K))

        # Solution 2:
        # O(nlong)
        # A.sort()  # O(nlogn)
        # return max(0, (A[-1] - K) - (A[0] + K))


sol = Solution()
A = [3, 1, 10]
K = 4
print(sol.smallestRangeI(A, K))
"""
A = [3, 1, 10]
K = 4

A = [1, 2, 100]
K = 2

Algorithm:
There is a key insight to get the smallest difference.

    First sort the elements of array A.
    2)Weneed to add the highest value of K to the smallest number in array A and we need to subtract the highest value of K from the biggest number in array A.
    The difference then would yield the smallest difference
    Ex: K = 2, A=[10,2,6,8,4], range of values of K= [-2,-1,0,1,2]
    A = [2,4,6,8,10] (After sorting)
    Add highest value of K to A[0] -> 2 + 2 = 4
    Subtract highest value of K from A[-1] -> 10 - 2 = 8
    Smallest difference = 8 - 4 = 4

"""
