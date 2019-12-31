"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:

    The given integer is guaranteed to fit within the range of a 32-bit signed integer.
    You could assume no leading zero bit in the integer’s binary representation.

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

"""


class Solution:
    def findComplement(self, num):
        # Solution 1: self
        # if not num:
        #     return num
        # n = bin(num).replace("0b", "")
        # com = ""
        # for i in range(len(n)):
        #     if n[i] == "0":
        #         com = com + "1"
        #     else:
        #         com = com + "0"

        # return int("".join(com), 2)

        # Solution 2: XOR
        # reference : https://leetcode.com/problems/number-complement/discuss/324332/Python-XOR-one-line-no-loops
        all_one = 2 ** (num.bit_length()) - 1
        result = num ^ all_one
        return result


sol = Solution()
n = 5
print(sol.findComplement(n))
