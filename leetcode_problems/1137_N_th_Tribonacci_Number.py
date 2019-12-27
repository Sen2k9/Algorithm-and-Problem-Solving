"""
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.



Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:

Input: n = 25
Output: 1389537



Constraints:

    0 <= n <= 37
    The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

"""


class Solution:

    def tribonacci(self, n: int):
        # Solution 1: iterative
        # arr = [0, 1, 1]
        # if n < 3:
        #     return arr[n]
        # t0 = arr[0]
        # t1 = arr[1]
        # t2 = arr[2]
        # tri = 0
        # for i in range(n - 2):
        #     tri = t0 + t1 + t2
        #     t0, t1 = t1, t2
        #     t2 = tri
        # return tri

        # Solution 2: using dictionary

        # tri = {0: 0, 1: 1, 2: 1}
        # if n < 3:
        #     return tri[n]

        # for i in range(3, n + 1):
        #     tri[i] = tri[i - 1] + tri[i - 2] + tri[i - 3]

        # return tri[n]

        # Solution 3: memory efficient
        tri = {}
        for i in range(n + 1):
            if i == 0:
                tri[i] = 0
            elif i == 1 or i == 2:
                tri[i] = 1
            else:
                tri[i] = tri[i - 1] + tri[i - 2] + tri[i - 3]

        return tri[n]


sol = Solution()
n = 25
print(sol.tribonacci(n))
"""
corner case:
although a recursion problem, recursion causes repetition, which is O(nlogn)
iterative process solves it with O(n) runtime
"""
