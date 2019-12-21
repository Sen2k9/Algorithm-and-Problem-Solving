"""
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

Note:

    The input array won't violate no-adjacent-flowers rule.
    The input array size is in the range of [1, 20000].
    n is a non-negative integer which won't exceed the input array size.

"""


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        # if len(flowerbed) < (2 * n) - 1:
        #     return False
        # left_zero = 0
        # right_zero = 0
        # mid_zero = 0
        # for _, val in enumerate(flowerbed):
        #     if val == 1:
        #         break
        #     left_zero += 1
        # n = n - left_zero // 2
        # # tackle the corner case of all elements are zero
        # if left_zero == len(flowerbed) and n == 1:
        #     return True
        # if n <= 0:
        #     return True
        # for _, val in enumerate(flowerbed[::-1]):
        #     if val == 1:
        #         break
        #     right_zero += 1
        # n = n - right_zero // 2
        # if n <= 0:
        #     return True
        # for i in range(left_zero, len(flowerbed) - right_zero):
        #     if flowerbed[i] == 0 and flowerbed[i+1] != 1:
        #         mid_zero += 1
        # n = n - (mid_zero) // 2
        # if n <= 0:
        #     return True

        # return False
        # Solution 1: efficient from leetcode
        length, index, count, bed = len(flowerbed) - 2, -2, 0, flowerbed + [0]

        while index < length:
            index = index + 2
            if bed[index] == 1:
                continue
            if bed[index + 1] == 0:
                count += 1
            else:
                index = index + 1
        return n <= count


sol = Solution()
flowerbed = [0, 1, 0, 0, 0, 1]
n = 1
print(sol.canPlaceFlowers(flowerbed, n))
"""
corner case:
1. first and last value is zero
2. all values are zero
3. [1,0,1,0,1,0,1]
4. abundant empty space than necessary > [0,0,0,0], n=1
"""
