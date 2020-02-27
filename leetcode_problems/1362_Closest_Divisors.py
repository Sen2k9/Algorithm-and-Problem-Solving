"""


Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

Return the two integers in any order.


Example 1:

Input: num = 8
Output: [3,3]
Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.

Example 2:

Input: num = 123
Output: [5,25]

Example 3:

Input: num = 999
Output: [40,25]

 

Constraints:

    1 <= num <= 10^9

"""


class Solution:
    def closestDivisors(self, num: int):
        import math
        l = []
        for i in range(1, int(math.ceil(math.sqrt(num))) + 2):
            # print(i)
            a = i
            b = int(math.ceil(num / a))

            if a * b == num + 1 or a * b == num + 2:
                l.append([a, b])
            if a * a == num + 1 or a * a == num + 2:
                l.append([a, a])
        # print(l)

        l = sorted(l, key=lambda x: abs(x[0] - x[1]))
        # print(l)
        return l[0]


sol = Solution()
num = 10
print(sol.closestDivisors(num))
