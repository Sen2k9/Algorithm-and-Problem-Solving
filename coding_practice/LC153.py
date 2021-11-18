import unittest


def find_min(arr):
    """
    """
    if not arr:
        return -1
    def find_max(arr):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if mid == len(arr) - 1 or arr[mid] > arr[mid + 1]:
                return mid
            elif arr[low] > arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
    
    idx = find_max(arr)
    if idx == len(arr) - 1:
        return arr[0]
    else:
        return arr[idx + 1]     


class TestFindMin(unittest.TestCase):

    def test_find_min(self):
        self.assertEqual(find_min([2,3,4,5,6,1]), 1)
        self.assertEqual(find_min([2,3,4,5,6,7]), 2)
        self.assertEqual(find_min([2,3,4,5,0,1]), 0)
        self.assertEqual(find_min([0,1]), 0)
        self.assertEqual(find_min([0]), 0)
        self.assertEqual(find_min([1]), 1)
        self.assertEqual(find_min([]), -1)

if __name__ == "__main__":
    unittest.main()
    