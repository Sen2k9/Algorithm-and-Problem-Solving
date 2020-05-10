class Solution:

    def buble_sort(self, arr):
        # time complexity : O(n^2)
        # Space complexity : O(1)

        for i in range(len(arr)):
            swaped = False
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

                    swaped = True
            if not swaped:
                break
        return arr

    def selection_sort(self, arr):
        # time complexity : O(n^2)
        # Space complexity : O(1)
        for i in range(len(arr)):
            key = arr[i]
            for j in range(i + 1, len(arr)):

                if key > arr[j]:
                    key = arr[j]
                    # keeping the smallest element at i from arr[i] to arr[n-1]
                    arr[i], arr[j] = arr[j], arr[i]

        return arr

    def insertion_sort(self, arr):
        # time complexity : O(n^2)
        # Space complexity : O(1)
        for i in range(1, len(arr)):
            j = i - 1
            key = arr[i]

            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key  # insert in the right position of left sub-array

        return arr

    def quick_sort(self, arr):
        # time complexity : O(n^2) if pivot is chosen as pivot = arr[high-1]
        # O(nlogn) if pivot is chosen pivot = arr[mid]
        # Space complexity : O(1)

        self.quick_sort_helper(0, len(arr), arr)

        return arr

    def quick_sort_helper(self, low, high, arr):

        def partition(arr, low, high):
            mid = (low+high)//2

            key = arr[mid]
            i = low - 1
            for j in range(low, high):
                if arr[j] < key:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i+1], arr[high-1] = key, arr[i + 1]
            return i+1

        if low < high:
            pivot = partition(arr, low, high)

            self.quick_sort_helper(low, pivot - 1, arr)
            self.quick_sort_helper(pivot+1, high, arr)

    def merge_sort(self, arr):
        # Time complexity : O(nlogn)
        # Space complexity : O(n)
        if len(arr) == 1:
            return arr

        low = 0
        high = len(arr)
        mid = (low + high) // 2

        left_arr = self.merge_sort(arr[:mid])
        right_arr = self.merge_sort(arr[mid:])

        new_arr = []
        i = j = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:

                new_arr.append(left_arr[i])
                i += 1
            else:
                new_arr.append(right_arr[j])
                j += 1

        if i < len(left_arr):
            new_arr = new_arr + left_arr[i:]

        if j < len(right_arr):
            new_arr = new_arr + right_arr[j:]

        return new_arr


sol = Solution()
arr = [12, 11, 13, 5, 6]
print("Bubble sort :", sol.buble_sort(arr))
print("Selection sort :", sol.selection_sort(arr))
print("Insertion sort :", sol.insertion_sort(arr))
print("Quick sort :", sol.quick_sort(arr))
print("Merge sort :", sol.merge_sort(arr))
"""
link : https://www.geeksforgeeks.org/sorting-algorithms/

https://www.quora.com/What-are-the-most-important-sort-algorithms
https://www.geeksforgeeks.org/lower-bound-on-comparison-based-sorting-algorithms/

"""
