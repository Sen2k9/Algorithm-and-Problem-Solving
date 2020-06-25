"""
Conversion:
Write a function to determine the number of bits you would need to flip to convert integer A to integer B.
EXAMPLE
Input : 29 , 15
Output : 2
"""


class Solution:

    def __init__(self):
        pass

    def conversion(self, A, B):

        mask = A ^ B
        count = 0

        while mask:
            if mask & 1 == 1:
                count += 1
            mask = mask >> 1
        return count


if __name__ == '__main__':
    sol = Solution()
    A = 8
    B = 7
    print(sol.conversion(A, B))

