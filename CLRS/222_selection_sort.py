class Solution:
    def selection_sort(self, A):
        if len(A) < 2:
            return A
        curr = A[0]
        j = 0
        index = 0
        while j < len(A) - 1:
            for i in range(j + 1, len(A)):
                if A[i] < curr:
                    curr = A[i]
                    index = i

            A[index] = A[j]
            A[j] = curr
            j += 1
            curr = A[j]
        return A


sol = Solution()
A = [2, 3, 10, 0, 1]
print(sol.selection_sort(A))
