"""
Pairwise Swap:
Write a program to swap odd and even bits in an integer with as few 
instruction as possible
(e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).
"""


class Solution:

    def __init__(self):
        pass

    def pairwise_swap(self, number):
        even_mask = 0xaaaaaaaa
        odd_mask = 0x55555555

        even_mask_applied = number & even_mask
        odd_mask_applied = number & odd_mask

        even_mask_applied = even_mask_applied >> 1
        odd_mask_applied = odd_mask_applied << 1

        return even_mask_applied | odd_mask_applied


if __name__ == '__main__':
    sol = Solution()
    print(sol.pairwise_swap(29))
