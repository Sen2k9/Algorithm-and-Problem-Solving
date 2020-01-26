class Solution:
    def N_fibonacci(self, n):
        # dic = {-1: 1, 0: 0, 1: 1}
        # for i in range(1, n + 1):
        #     dic[i] = dic[i-1]+dic[i-2]

        #     print("{} = {}".format(i, dic[i]))
        # O(n)

        # terrible algorithm
        # def fib(a):
        #     if a <= 0:
        #         return 0
        #     elif a == 1:
        #         return 1

        #     else:
        #         return fib(a - 1) + fib(a - 2)
        # # return fib(n)
        # for i in range(1, n + 1):
        #     print("{} = {}".format(i, fib(i)))

        # using memorization

        def memo_fib(n, memo):
            if n <= 0:
                return 0
            elif n == 1:
                return 1
            elif memo[n] > 0:
                return memo[n]
            memo[n] = memo_fib(n - 1, memo) + memo_fib(n - 2, memo)
            return memo[n]
        self.memo = [0 for i in range(n+1)]  # O(n)
        for i in range(1, n + 1):  # O(2n)

            print("{} = {}".format(i, memo_fib(i, self.memo)))

        # overall O(n) + O(2n) = O(n)


sol = Solution()
n = 10
print(sol.N_fibonacci(n))
