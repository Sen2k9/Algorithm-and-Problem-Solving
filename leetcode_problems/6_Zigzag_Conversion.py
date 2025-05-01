"""
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"

 

Constraints:

    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000


"""
import unittest

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # N = number of Rows
        # first and last row follows the pattern N + (N - 2) to get all element
        # middle rows get some values using pattern N + (N - 2)
        # other values for middle rows need to use 2r + N + (N - 2)
        if numRows == 1:
            return s
        answer = []

        for row in range(numRows):
            if row == 0 or row == numRows - 1:
                start = row
                while start < len(s):
                    answer.append(s[start])
                    start = start + numRows + (numRows - 2)
            
            else:
                first = row
                second = first + numRows + (numRows - 2) - (2 * row)

                while first < len(s):
                    answer.append(s[first])
                    if second < len(s):
                        answer.append(s[second])

                    first = first + numRows + (numRows - 2)
                    second = first + numRows + (numRows - 2) - (2 * row)
        #print(answer)
        return "".join(answer)
    
class TestSuite(unittest.TestCase):
    def test_palindrome(self):
        sol = Solution()
        self.assertEqual(sol.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(sol.convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")


if __name__ == "__main__":
    unittest.main()