def find_single_number(arr):
  ans = 0
  for each in arr:
    ans = ans ^ each
  return ans

import unittest

class TestSolution(unittest.TestCase):

    def test_find_single_number(self):
        arr = [1, 4, 2, 1, 3, 2, 3]
        self.assertEqual(
            find_single_number(arr),
            4
        )

if __name__ == '__main__':
    unittest.main()