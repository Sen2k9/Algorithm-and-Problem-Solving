"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""


class Solution:
    def numSquares(self, n: int):
        import math
        check_square = []
        for i in range(1, int(n ** 0.5) + 1):
            check_square.append(i**2)

        queue = set()
        queue.add(n)
        level = 0

        while queue:
            new_queue = set()
            level += 1
            for each in queue:
                if each in check_square:
                    return level
                for square in check_square:
                    if each < square:
                        break
                    elif each - square in new_queue:
                        continue
                    else:
                        new_queue.add(each - square)
            queue = new_queue
            #print(queue, check_square)


sol = Solution()
n = 13
print(sol.numSquares(n))
