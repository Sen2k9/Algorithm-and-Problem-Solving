import math


class Solution:
    def isPrime(self, n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


sol = Solution()
n = 31
print(sol.isPrime(n))
