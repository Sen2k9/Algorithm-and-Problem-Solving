"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

"""


class Solution:
    def fourSumCount(self, A, B, C, D):
        sumAB = {}
        sumCD = {}
        for i in range(len(A)):
            for j in range(len(B)):
                temp = A[i] + B[j]
                if temp in sumAB:
                    sumAB[temp] += 1
                else:
                    sumAB[temp] = 1

                tempCD = C[i] + D[j]
                if tempCD in sumCD:
                    sumCD[tempCD] += 1
                else:
                    sumCD[tempCD] = 1
        count = 0
        print(sumAB, sumCD)
        for key in sumAB.keys():
            if - key in sumCD:
                count += sumAB[key]*sumCD[-key]
        return count


sol = Solution()
A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
print(sol.fourSumCount(A, B, C, D))
