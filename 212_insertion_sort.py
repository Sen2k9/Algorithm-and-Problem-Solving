class Solution:
    def Increasing_Insertion_Sort(self, A):
        for j in range(1, len(A)):
            val = A[j]
            i = j - 1
            while i >= 0 and A[i] > val:
                A[i + 1] = A[i]
                i = i - 1
                # print(A)

            A[i+1] = val

        return A

    def Decreasing_Insertion_Sort(self, A):
        for j in range(1, len(A)):
            val = A[j]
            i = j - 1

            while i >= 0 and A[i] < val:
                A[i + 1] = A[i]
                i = i - 1
            A[i + 1] = val
        return A


sol = Solution()
A = [5, 2, 4, 6, 1, 3]
print(sol.Increasing_Insertion_Sort(A))
print(sol.Decreasing_Insertion_Sort(A))
"""
for each value compares all other values before it,
So in worst case O(n^2)
"""
