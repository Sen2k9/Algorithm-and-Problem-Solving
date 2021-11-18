import unittest
import itertools

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def return_filtered_str(string):
            backspace_count = 0
            for i, char in enumerate(reversed(string)):
                if char == '#':
                    backspace_count += 1

                elif backspace_count:
                    backspace_count -= 1
                else:
                    yield char
        
        
        return all(x == y for x, y in itertools.zip_longest(return_filtered_str(s), return_filtered_str(t)))


class TestFindMin(unittest.TestCase):

    def test_backspaceCompare(self):
        sol = Solution()
        self.assertEqual(sol.backspaceCompare('ab#c', 'ad#c'), True)

if __name__ == "__main__":
    unittest.main()
    