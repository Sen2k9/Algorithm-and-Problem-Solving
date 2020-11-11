"""
 Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100]. 
"""


class Solution:
    def dailyTemperatures(self, T):
        # using stack

        ans = [0] * len(T)

        stack = [(T[0], 0)]

        for i in range(1, len(T)):
            print(stack)
            while stack and stack[-1][0] < T[i]:
                ans[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((T[i], i))

        return ans
            




sol = Solution()
T = [73, 74, 75, 71, 69, 72, 76, 73]
print(sol.dailyTemperatures(T))