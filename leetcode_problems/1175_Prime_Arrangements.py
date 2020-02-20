"""
Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:

Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.

Example 2:

Input: n = 100
Output: 682289015

Constraints:

    1 <= n <= 100

"""


class Solution:
    def numPrimeArrangements(self, n: int):
        # Solution 1: brute-force
        import math
        if n < 3:
            return 1
        total_prime = []
        for val in range(2, n + 1):
            for i in range(2, int(math.sqrt(val))+1):
                if val % i == 0:
                    break
            else:
                total_prime.append(val)
        # print(total_prime)
        composite = n - len(total_prime)
        # print(composite)

        return (math.factorial(len(total_prime))*math.factorial(composite)) % (10**9 + 7)
        # Solution: using Sieve technique for finding prime
        import math
        if n < 3:
            return 1

        def simple_sieve(n, primes):
            mark = [False] * (n + 1)
            for i in range(2, int(math.sqrt(n)) + 1):
                if not mark[i]:
                    primes.append(i)
                    for j in range(i*2, n + 1, i):
                        mark[j] = True
            for i in range(int(math.sqrt(n))+1, n + 1):
                if not mark[i]:
                    primes.append(i)

            return primes

        total_primes = list()
        total_primes = simple_sieve(n, total_primes)
        print(total_primes)
        composite = n - len(total_primes)
        return (math.factorial(len(total_primes))*math.factorial(composite)) % (10**9 + 7)


sol = Solution()
n = 5
print(sol.numPrimeArrangements(n))
