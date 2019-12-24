"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


"""


class Solution:
    def climbStairs(self, n):
        # Solution 1:
        # if n == 0:
        #     return 0
        # elif n == 1:
        #     return 1
        # arr = [0] * n
        # arr[0] = 1
        # arr[1] = 2
        # for i in range(2, n):
        #     arr[i] = arr[i - 1] + arr[i - 2]
        # return arr[n-1]

        # Solution 2: space efficient, no new array assignment,
        # if n <= 2:
        #     return n
        # first = 1
        # second = 2
        # result = 0
        # for _ in range(3, n+1):
        #     result = first + second
        #     first = second
        #     second = result
        # return result

        # Solution 3: Faster, using recursion, memorization
        memo = {}
        return self.climbStairsHelper(n, memo)

    def climbStairsHelper(self, n, memo):
        if n <= 2:
            return n
        if n in memo:
            # print(memo[n])
            return memo[n]
        else:
            memo[n] = self.climbStairsHelper(
                n - 1, memo) + self.climbStairsHelper(n - 2, memo)
        return memo[n]


sol = Solution()
n = 6
print(sol.climbStairs(n))
"""
corner case:
1. n = 1 or n = 0
"""
