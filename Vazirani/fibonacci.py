class Solution:
    def fib1(self, n):  # exponential algorithm, can not compute n = 100 with recursive
        if n <= 0:
            return 0
        if n == 1:
            return 1

        return self.fib1(n - 1) + self.fib1(n - 2)

    def fib2(self, n):  # linear algorithm O(n)
        if n <= 0:
            return 0
        f = [0] * (n + 1)
        f[0] = 0
        f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]


sol = Solution()
n = 100
print(sol.fib2(n))
