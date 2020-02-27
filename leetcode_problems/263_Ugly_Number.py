"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3

Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2

Example 3:

Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another prime factor 7.

Note:

    1 is typically treated as an ugly number.
    Input is within the 32-bit signed integer range: [−231,  231 − 1].
"""


class Solution:
    def isUgly(self, num: int):
        # if num == 1:
        #     return True
        # import math
        # l = [False] * (num + 1)
        # prime = set()
        # for i in range(2, int(math.sqrt(num)) + 1):
        #     if num % i == 0 and l[i] == False:
        #         prime.add(i)
        #     for j in range(i * 2, num + 1, i):
        #         l[j] = True
        # for i in range(2, num + 1):
        #     if not l[i] and num % i == 0:
        #         # print(i)
        #         if i != 2 and i != 3 and i != 5:
        #             return False

        # return True

        # Solution 2: fastest
        if num == 1:
            return True

        if num == 0:
            return False

        primes = [2, 3, 5]

        for each in primes:
            while num % each == 0:
                num = num//each

        if num == 1:
            return True
        else:
            return False


sol = Solution()
num = 8
print(sol.isUgly(num))
