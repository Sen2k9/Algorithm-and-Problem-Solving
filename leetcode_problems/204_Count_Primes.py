"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""


class Solution:
    def countPrimes(self, n: int):
        arr = [1] * n
        arr[0] = 0
        arr[1] = 0
        i = 2
        while i * i < n:
            if arr[i] == 1:

                for j in range(i*i, n, i):
                    arr[j] = 0
            i += 1
        return sum(arr)


sol = Solution()
n = 10
print(sol.countPrimes(n))

"""
reference:
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

https://leetcode.com/problems/count-primes/discuss/435363/Python3-Simple-Code-How-to-Make-Your-Code-Faster.

"""
