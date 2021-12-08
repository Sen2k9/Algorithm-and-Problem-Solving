def find_subsets(nums):
    subsets = [[]]
    for num in nums:
        subsets += [curr + [num] for curr in subsets]
        print(subsets)

    return subsets

import unittest

class TestSolution(unittest.TestCase):
    def test_find_subsets(self):
        print("Here is the list of subsets: " + str(find_subsets([1, 3])))
        print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


if __name__ == '__main__':
    unittest.main()