"""
Two-dimensional Version
a is a 2D-peak iff a ≥ b, a ≥ d, a ≥ c, a ≥ e
"""


class Solution:
    def peakfinder(self, nums):

        def peak_1D(temp):

            big = -float("Inf")

            for i in range(len(temp)):  # O(n)
                if temp[i] > big:
                    big = temp[i]

            return big

        m = len(nums[0])  # column

        # binary search

        i = 0
        j = m-1
        while i <= j:
            mid = (i+j)//2

            global_peak = peak_1D(nums[:][mid])

            if mid-1 >= 0 and global_peak < peak_1D(nums[:][mid - 1]):
                j = mid - 1
            elif mid+1 <= m-1 and global_peak < peak_1D(nums[:][mid + 1]):
                i = mid + 1
            else:
                return global_peak


sol = Solution()
nums = [[10, 20, 15],
        [21, 30, 14],
        [7, 16, 32]]

# nums = [[10, 8, 10, 10],
#         [14, 13, 12, 11],
#         [15, 9, 11, 21],
#         [16, 17, 19, 20]]
print(sol.peakfinder(nums))
"""
references:

"""
