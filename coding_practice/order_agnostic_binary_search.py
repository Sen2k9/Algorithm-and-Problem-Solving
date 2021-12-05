def is_ascending(arr):
    return arr[0] <= arr[-1]

def binary_search(arr, key):
    ascending = True if is_ascending(arr) else False

    low = 0
    high = len(arr) - 1

    while low <= high:
        #mid = (low + high) // 2 # this will cause integer overflow for other languages
        # safe
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            if ascending:
                high = mid - 1
            else:
                low = mid + 1
        elif arr[mid] < key:
            if ascending:
                low = mid + 1
            else:
                high = mid - 1
    return -1

import unittest


class TestSolution(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(
            binary_search([4, 6, 10], 10),
            2
        )
        self.assertEqual(
            binary_search([1, 2, 3, 4, 5, 6, 7], 5),
            4
        )
        self.assertEqual(
            binary_search([10, 6, 4], 10),
            0
        )
        self.assertEqual(
            binary_search([10, 6, 4], 4),
            2
        )

if __name__ == '__main__':
    unittest.main()