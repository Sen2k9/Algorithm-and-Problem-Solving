"""
The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.

Given a positive integer N, return true if and only if it is an Armstrong number.

Example 1:

Input: 153
Output: true
Explanation: 
153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.

Example 2:

Input: 123
Output: false
Explanation: 
123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.

Note:

    1 <= N <= 10^8
"""


class Solution:
    def isArmstrong(self, N: int):
        # Solution 1:
        # Time : O(log10(n))
        # Space : O(1)

        # length = len(str(N))
        # n = N
        # total = 0
        # while n > 0:

        #     total = total + (n % 10) ** length
        #     n = n // 10
        #     #print(n, total)
        #     if total > N:
        #         return False
        # return True if total == N else False

        # Solution 2: one-liner
        # Time : O(log10(n))
        # Space : O(1)

        return sum([i**len(str(N)) for i in map(int, str(N))]) == N


sol = Solution()
N = 123
print(sol.isArmstrong(N))
