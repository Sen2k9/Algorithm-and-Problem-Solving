"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15

Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21

 

Constraints:

    1 <= n <= 10^5

"""


class Solution:
    def subtractProductAndSum(self, n):

        l = list(str(n))
        if len(l) == 1:
            return 0

        if "0" in l:
            product = 0
        else:
            product = 1
        total = 0
        for each in l:
            if each == "0":
                continue

            total += int(each)
            product = product * int(each)
        return product - total


sol = Solution()
n = 9999
print(sol.subtractProductAndSum(n))
"""
corner case:
1. if any digit is zero, product zero
2. if n is only one digit
"""
