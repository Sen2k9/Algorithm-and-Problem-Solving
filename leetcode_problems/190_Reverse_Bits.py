"""
Reverse bits of a given 32 bits unsigned integer.
Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.

Note:

    Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
    In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above the input represents the signed integer -3 and the output represents the signed integer -1073741825.

Follow up:

If this function is called many times, how would you optimize it?
"""


class Solution:
    def reverseBits(self, n: int):
        # Solution 1: self, brute-force

        # s = list(bin(n & 0xffffffff).replace("0b", ""))
        # s = ["0"]*(32-len(s))+s
        # s = s[::-1]
        # # print(s)
        # # print(s,"".join(s))
        # return int("".join(s), 2)

        # solution 2: recommended

        reverse_bit = 0

        for _ in range(32):
            reverse_bit = reverse_bit << 1

            reverse_bit = reverse_bit | (n & 1)
            n = n >> 1

        return reverse_bit

        # Solution 3: not recommended

        # return int('{0:032b}'.format(n)[::-1], 2)


sol = Solution()
n = 43261596
print(sol.reverseBits(n))
"""
reference:
https://leetcode.com/problems/reverse-bits/discuss/468824/Python-O(-1-)-sol.-based-on-bit-manipulation
https://leetcode.com/problems/reverse-bits/discuss/422384/Python-Accepted-Answer%3A-One-Liner%3A-int('0%3A032b'.format(n)%3A%3A-1-2)
"""
