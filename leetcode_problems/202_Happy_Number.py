"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution:
    def isHappy(self, n: int):
        # Solution 1: self
        # if n == 1:
        #     return True
        # dic = {n}
        # digits = []

        # while True:
        #     d, a = divmod(n, 10)
        #     print(dic, n)
        #     if a == 0 and d == 0:

        #         total = 0
        #         for each in digits:
        #             total += each**2
        #         n = total

        #         digits.clear()

        #         if total in dic:
        #             return False
        #         elif total == 1:
        #             return True
        #         dic.add(n)

        #     else:
        #         digits.append(a)
        #         n = d

        # Solution 2: clean, faster
        dic = {"0": 0, "1": 1, "2": 4, "3": 9, "4": 16,
               "5": 25, "6": 36, "7": 49, "8": 64, "9": 81}
        seen = {n}
        total = sum(dic[x] for x in str(n))
        while total != 1:
            print(seen)

            if total in seen:
                return False
            else:
                seen.add(total)
                total = sum(dic[x] for x in str(total))

        return True


sol = Solution()
n = 4
print(sol.isHappy(n))
