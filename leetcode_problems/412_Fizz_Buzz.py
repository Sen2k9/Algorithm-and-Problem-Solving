"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""


class Solution:
    def fizzBuzz(self, n: int):
        # Solution 1:
        # runtime: O(n)
        # space : O(n)
        # arr = []
        # for i in range(1, n+1):
        #     if i % 3 == 0 and i % 5 == 0:
        #         arr.append("FizzBuzz")
        #     elif i % 3 == 0:
        #         arr.append("Fizz")
        #     elif i % 5 == 0:
        #         arr.append("Buzz")
        #     else:
        #         arr.append(str(i))
        # return arr

        # Solution 2: one-liner
        # Runtime: O(n)
        # space : O(1)

        # return ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for i in range(1, n + 1)]

        # Solution 3: fun with list-comprehension
        return ["Fizz"*(i % 3 == 0)+"Buzz"*(i % 5 == 0)or str(i) for i in range(1, n+1)]


sol = Solution()
n = 15
print(sol.fizzBuzz(n))
"""
reference:
https://leetcode.com/problems/fizz-buzz/discuss/493072/Python-O(-n-)-sol.-by-list-comprehension-and-iteration.-With-explanation
"""
