class Solution:

    def __init__(self):
        pass

    def insertion(self, m, n, i, j):

        leftmask = ~0 << (j + 1)
        rightmask = (1 << i) - 1
        mask = leftmask | rightmask

        n = n & mask

        m = m << i

        return n | m


if __name__ == '__main__':
    n = 2048
    print(bin(n))
    m = 19
    print(bin(m))
    i = 2
    j = 6

    sol = Solution()
    ans = sol.insertion(m, n, i, j)
    print(bin(ans))
