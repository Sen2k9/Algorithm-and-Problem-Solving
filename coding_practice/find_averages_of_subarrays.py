def find_averages_of_subarrays(arr, k):
    if k == 0:
        return []
    _sum = sum(arr[:k])
    ans = [(_sum) / k]
    start = 1
    end = k
    while end < len(arr):
        _sum = _sum - arr[start - 1] + arr[end]
        ans.append((_sum) / k)
        start += 1
        end += 1
        #print(ans)
    return ans

import unittest

class TestSolution(unittest.TestCase):

    def test_find_averages_of_subarrays(self):
        self.assertEqual(
            find_averages_of_subarrays
                [1, 3, 2, 6, -1, 4, 1, 8, 2],
                5
            ),
            [2.2, 2.8, 2.4, 3.6, 2.8]
        )

if __name__ == '__main__':
    unittest.main()