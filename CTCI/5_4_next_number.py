"""
Next number:
Given a positive integer, print the next smallest and the next largest number
that have the same number of 1 bits in their binary representation.
"""


class Solution:
    def __init__(self):
        pass

    def next_number(self, number):

        return self.getNext(number), self.getPrevious(number)

    def getNext(self, number):
        c0 = 0
        c1 = 0
        c = number

        while (c & 1) == 0 and c != 0:
            c0 += 1
            c >>= 1

        while (c & 1) == 1:
            c1 += 1
            c >>= 1
        p = c1 + c0

        flip_bit = 1 << p
        number = number | flip_bit

        mask = flip_bit - 1

        number = number & (~mask)

        a = 1 << (c1 - 1)
        b = a - 1
        mask = b << (c0 + 1)

        number = number | mask

        return number

    def getPrevious(self, number):
        c0 = 0
        c1 = 0
        c = number

        while (c & 1) == 1:
            c1 += 1
            c >>= 1
        if c == 0:
            return -1
        while (c & 1) == 0 and c != 0:
            c0 += 1
            c >>= 1

        p = c1 + c0

        a = ~0 << p+1

        number = number & a
        # print(number)

        a = 1 << (c1+1)
        b = a - 1
        mask = b << (c0 - 1)
        number = number | mask

        return number


if __name__ == '__main__':
    sol = Solution()
    print(sol.next_number(16))
