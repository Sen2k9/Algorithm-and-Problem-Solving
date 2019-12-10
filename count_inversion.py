import pdb


class Solution:
    def merge_sort(self, number):
        if len(number) == 1:
            return number

        n = len(number)
        m = n // 2
        left = number[0:m]
        right = number[m:]

        left_merge = self.merge_sort(left)
        right_merge = self.merge_sort(right)

        i = 0
        j = 0
        k = 0
        arr = [0]*len(number)
        while i < len(left_merge) and j < len(right_merge):
            if left_merge[i] < right_merge[j]:
                arr[k] = left_merge[i]
                k += 1
                i += 1
            else:
                arr[k] = right_merge[j]
                k += 1
                j += 1
        while i < len(left_merge):
            arr[k] = left_merge[i]
            i += 1
            k += 1

        while j < len(right_merge):
            arr[k] = right_merge[j]
            j += 1
            k += 1

        return arr

    def merge_split(self, numbers):
        n = len(numbers)
        m = n // 2
        left = numbers[0:m]
        right = numbers[m:]

        left_inv = self.merge_sort(left)
        right_inv = self.merge_sort(right)
        # pdb.set_trace()

        i = 0
        j = 0
        inversion = 0
        while i < len(left_inv) and j < len(right_inv):
            if left_inv[i] > right_inv[j]:
                inversion = inversion + (len(left_inv) - i)
                j += 1
            else:
                i += 1

        return inversion


sol = Solution()
numbers = [1, 3, 5, 2, 4, 6]
print(sol.merge_split(numbers))
