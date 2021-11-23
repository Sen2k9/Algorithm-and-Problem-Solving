import unittest


class Solution:

    def find_missing_number(self, arr):
        all_numbers = len(arr) + 1
        x1 = 1
        for each in range(2, all_numbers + 1):
            x1 = x1 ^ each
        x2 = arr[0]
        for i in range(1, len(arr)):
            x2 = x2 ^ arr[i]
        
        return x1 ^ x2


class TestSolution(unittest.TestCase):

    def test_find_missing_number(self):
        arr = [1, 5, 2, 6, 4]
        sol = Solution()
        ans = sol.find_missing_number(arr)
        self.assertTrue(ans)
        print('Missing number is:' + str(ans))


if __name__ == '__main__':
    unittest.main()