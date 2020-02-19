class Solution:
    def add_binary(self, A, B):
        # O(n)
        C = [0] * (len(A))
        carry = 0

        for i in range(len(A) - 1, -1, -1):
            if (A[i] + B[i] + carry) == 2:
                C[i] = 0
                carry = 1
            else:
                C[i] = A[i] + B[i] + carry
                carry = 0

        if carry == 1:
            return [1] + C
        else:
            return C


sol = Solution()
A = [1, 0, 1, 1, 0, 1]
B = [1, 0, 0, 0, 1, 1]
print(sol.add_binary(A, B))
