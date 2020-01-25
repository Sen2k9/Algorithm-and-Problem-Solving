"""
 Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

    All letters in hexadecimal (a-f) must be in lowercase.
    The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
    The given number is guaranteed to fit within the range of a 32-bit signed integer.
    You must not use any method provided by the library which converts/formats the number to hex directly.

Example 1:

Input:
26

Output:
"1a"

Example 2:

Input:
-1

Output:
"ffffffff"
"""


class Solution:
    def toHex(self, num: int):
        # Solution 1: self, fastest
        s = bin(num & 0xffffffff).replace("0b", "")
        print(s)
        res = ""
        for i in range(len(s), -1, -4):
            if s[0:i] and len(s[0:i]) < 4:

                res = str(int(s[0:i], 2)) + res
            elif len(s[i-4:i]) > 0:
                print(s[i-4:i])

                a = int(s[i-4:i], 2)
                if a > 9:

                    c = chr(97 + a - 10)
                else:
                    c = str(a)
                res = c + res
        return res


sol = Solution()
num = 8
print(sol.toHex(num))
