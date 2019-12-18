"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

"""


class Solution:
    def plusOne(self, digits):
        plus = 1
        for i in range(len(digits)-1, -1, -1):
            d, m = divmod(digits[i] + plus, 10)
            digits[i] = m
            print(d, m)
            if m != 0:
                break
        while m == 0:
            d, m = divmod(d, 10)
            digits = [m] + digits
        return digits


sol = Solution()
digits = [9, 9, 9]
print(sol.plusOne(digits))
"""
corner case:
digits = [9,9,9]
"""
