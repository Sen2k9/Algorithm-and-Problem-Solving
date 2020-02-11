"""Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""


class Solution:
    def addDigits(self, num: int):
        # Solution 1: iterative, self
        # Runtime : O(n), where n is the number of digits
        # Space : O(n)
        s = str(num)
        while num > 9:
            result = 0
            for each in s:
                result += int(each)
            num = result
            s = str(num)
        return int(s)

        # Solution 2: recursion
        # Runtime : O(n), where n is the number of digits
        # Space : O(n)
        if num <= 9:
            return num
        result = 0
        for each in str(num):
            result += int(each)
        return self.addDigits(result)

        # Solution 3: fastest, finding pattern using brute-force
        # O(1)
        # O(1)
        if num < 9:  # any number below 9 is one digit
            return num
        else:
            if num % 9 != 0:  # numbers who are not divisible by 9 their digital root is the modulus result by 9
                # example: 38 > 3+8 > 1+1 > 2
                # 38 % 9 = 2
                return num % 9
            else:
                return 9  # all numbers divisible by 9 have digital root as 9
                # example : 729 > 9+9 > 1+8 > 9
                # 729//9 = 9

        # Solution 4: digital root formula

        if num == 0:
            return 0
        else:
            return (num-1) % (10-1)+1


sol = Solution()
num = 15
print(sol.addDigits(num))
"""
reference:

digital root formula for base b: use Congruence formula for easy understand
https://en.wikipedia.org/wiki/Digital_root
"""
