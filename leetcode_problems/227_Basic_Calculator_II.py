"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7

Example 2:

Input: " 3/2 "
Output: 1

Example 3:

Input: " 3+5 / 2 "
Output: 5

Note:

    You may assume that the given expression is always valid.
    Do not use the eval built-in library function.

"""

class Solution:
    def calculate(self, s: str) -> int:
        
        if not s:
            return 0

        # initialization
        stack = []
        num = 0
        sign = "+"

        for index in range(len(s)):

            if s[index].isdigit():
                num = num * 10 + ord(s[index]) - ord("0")

            if not s[index].isdigit() and not s[index].isspace() or index == len(s) - 1:

                if sign == "+":
                    stack.append(num)
                
                elif sign == "-":
                    stack.append(-num)

                elif sign == "*":
                    stack.append(stack.pop() * num)

                elif sign == "/":

                    temp = stack.pop()

                    if temp // num < 0:
                        #print(temp // num, temp, num)
                        stack.append(-((-temp) //  num))

                    else:
                        stack.append(temp // num)

                sign = s[index]
                num = 0
            #print(stack)

        
        return sum(stack)

sol = Solution()
s = " 3+5 / 2 "

print(sol.calculate(s))

# special case
s = "14-3/2"
print(sol.calculate(s))