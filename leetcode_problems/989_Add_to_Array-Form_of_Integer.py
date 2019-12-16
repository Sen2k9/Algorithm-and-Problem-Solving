"""
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

 

Example 1:

Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234

Example 2:

Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

Example 3:

Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021

Example 4:

Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000

 

Note：

    1 <= A.length <= 10000
    0 <= A[i] <= 9
    0 <= K <= 10000
    If A.length > 1, then A[0] != 0


"""


class Solution():
    def addToArrayForm(self, A, K):

        # Solution 1: brute-force
        # if len(A) < 1:
        #     return k
        # a = ''
        # for each in A:
        #     a = a + str(each)
        # total = int(a) + k
        # final = []
        # for each in str(total):
        #     final.append(int(each))
        # return final

        # Solution 2: Best Solution
        for i in range(len(A) - 1, -1, -1):
            if not K:
                break
            K, A[i] = divmod(A[i] + K, 10)
            print(K, A[i], A)
        while K:
            K, a = divmod(K, 10)
            A = [a] + A
        return A


sol = Solution()
A = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
K = 1
print(sol.addToArrayForm(A, K))
"""
corner case:
1. only one element
Notes:

    Leetcode provided a simple solution, but it is not efficient. K has 5 digits at most, but A can have 10000 elements. This means that the summation might finish after 5 iterations, but the loop will continue for 10000 times! I added a condition to avoid this.
    I think the purpose of this question is to provide a summation based on elementary school math, and avoid other functions such as 'str', 'int' and 'map'.
    The Leetcode solution does not work for Python3, but slight changes would make it compatible for both Python/ Python3.

"""
