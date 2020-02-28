"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

Input: 3
Output: False
"""


class Solution:
    def judgeSquareSum(self, c: int):
        # Solution : two pointer
        # Time : O(sqrt(n))
        # Space : O(1)
        # left = 0
        # right = int(c ** 0.5)
        # while left <= right:
        #     result = left ** 2 + right ** 2
        #     if result == c:
        #         return True
        #     elif result < c:
        #         left += 1
        #     elif result > c:
        #         right -= 1
        # return False

        # Solution 2: using set
        # Time : O(sqrt(n))
        # Space: O(sqrt(n))

        # possible_squares = set()

        # i = 0
        # while i * i <= c:
        #     possible_squares.add(i * i)
        #     i += 1

        # for v in possible_squares:
        #     if (c - v) in possible_squares:
        #         return True
        # return False
        n = c
        i = 2
        while (i * i <= n):
            print(i)
            count = 0
            if (n % i == 0):

                # Count all the prime factors.
                while (n % i == 0):
                    count += 1
                    n = int(n / i)

                # Ifany prime factor of the
                # form (4k+3)(4k+3) occurs
                # an odd number of times.
                if (i % 4 == 3 and count % 2 != 0):
                    return False
            i += 1

        # If n itself is a x prime number and
        # can be expressed in the form of 4k + 3
        # we return false.
        return n % 4 != 3


sol = Solution()
c = 10

print(sol.judgeSquareSum(c))

"""
https://leetcode.com/problems/sum-of-square-numbers/discuss/353607/Python-Easy-Solution%3A-Two-Pointers
https://leetcode.com/problems/sum-of-square-numbers/discuss/487621/Python-sol.-based-on-%22Sum-of-two-squares-theorem%22-95%2B-With-explanation
"""
