"""
 Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:

Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:

Input: 9973
Output: 9973
Explanation: No swap.

Note:

    The given number is in the range [0, 108]


"""


class Solution:
    def maximumSwap(self, num: int):
        # Solution 1:
        # time-complexity : O(n^2)
        # space : O(n)
        # if num < 10:
        #     return num

        # else:

        #     digits = list(str(num))

        #     i = 0
        #     max_digits = (-1, -1)
        #     print(digits)

        #     while i < len(digits):

        #         for j in range(i, len(digits)):
        #             if int(digits[j]) >= max_digits[1]:
        #                 max_digits = (j, int(digits[j]))

        #         if int(digits[i]) == max_digits[1]:
        #             i += 1
        #             max_digits = (-1, -1)

        #         else:
        #             print(max_digits)
        #             digits[i], digits[max_digits[0]
        #                               ] = digits[max_digits[0]], digits[i]
        #             break

        #     return int("".join(digits))

        # Solution 2:
        # time-complexity : O(n)
        if num < 10:
            return num

        else:
            # O(n)
            digits = list(str(num))

            last_occurance = [0] * 10

            # O(n)
            for i in range(len(digits)):
                last_occurance[ord(digits[i]) - ord('0')] = i

            # 10* O(n) ~ O(n)
            for i in range(len(digits)):

                for j in range(9, int(digits[i]), -1):
                    if last_occurance[j] > i:
                        digits[i], digits[last_occurance[j]
                                          ] = digits[last_occurance[j]], digits[i]

                        return int("".join(digits))

            return int("".join(digits))


sol = Solution()
num = 1993

print(sol.maximumSwap(num))

"""
corner case:
1. less than 10
2. 98368 when scanning the number from left to right, if there is a larger digit in the future, we will swap it with the largest such digit;
3. 1993 if there are multiple such digits, we will swap it with the one that occurs the latest.
"""
