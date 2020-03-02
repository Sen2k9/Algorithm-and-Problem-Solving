"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x: int):
        # Solution 1: using math.log
        # Runtime: O(number of digits)
        # Space : O(1)
        import math

        def countbits(number):
            count = int(math.log(number, 2)) + 1
            if count >= 32:
                return 0
            else:
                return number

        if x == 0:
            return 0
        s = str(x)
        if x < 0:
            n = int(s[1:][::-1])
            return int("-"+str(countbits(n)))
        else:
            n = int(s[::-1])
            return countbits(n)

        # Solution 2: using list
        # if x == 0:
        #     return 0

        # list_x = list(str(x))

        # if list_x[0] == "-":  # negative sign
        #     list_x = [list_x[0]] + list(reversed(list_x[1:]))
        # else:
        #     list_x = list(reversed(list_x))

        # number = "".join(list_x)
        # # print(number)

        # if - 2 ** 31 > int(number) or int(number) > (2 ** 31 - 1):
        #     return 0
        # else:
        #     return int(number)


sol = Solution()
x = -234
print(sol.reverse(x))
"""
references:

https://leetcode.com/problems/reverse-integer/discuss/507396/Easy-Python-w-comments-beats-98

https://www.geeksforgeeks.org/count-total-bits-number/
"""
