"""
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

Example 1:

Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:

Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Example 3:

Input: "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".

"""


class Solution:
    def removeOuterParentheses(self, S: str):
        # Solution 1: self, two-pointer
        # result = ""
        # i = 0
        # j = 0
        # count = 0

        # while i < len(S) and j < len(S):
        #     if S[j] == "(":
        #         count += 1

        #     else:
        #         count -= 1
        #     if count == 0:
        #         result = result + S[i + 1:j]
        #         i = j+1
        #     j += 1
        # return result

        # Solution 2: in-place traversal
        # result = ""
        # count = 0
        # for each in S:
        #     if each == "(":
        #         count += 1
        #         if count > 1:
        #             result += each
        #     elif each == ")":
        #         count -= 1
        #         if count > 0:
        #             result += each
        # return result

        # Solution 3: using stack concept

        result = current = ""
        stack = []

        for each in S:
            if stack and stack[-1] == "(" and each == ")":
                stack.pop()
            else:
                stack.append(each)

            current += each

            if not stack:
                result = result + current[1:-1]
                current = ""
        return result


sol = Solution()
S = "(()())(())"
print(sol.removeOuterParentheses(S))

"""
common stack, two pointer concept
"""
