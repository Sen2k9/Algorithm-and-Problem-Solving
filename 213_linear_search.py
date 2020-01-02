class Solution:
    def linear_search(self, A, v):
        # O(n)
        for i, val in enumerate(A):
            if val == v:
                return i
        return -1


sol = Solution()
A = [31, 41, 59, 26, 41, 58]
v = 27
print(sol.linear_search(A, v))
