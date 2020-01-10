"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!

Example :
Input: n = 10, pick = 6
Output: 6

"""
# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int):
        if n < 2:
            return n
        i = 1
        j = n

        while i <= j:
            mid = (i+j)//2
            if guess(mid) ==-1:
                j = mid-1
            elif guess(mid) == 1:
                i = mid+1
            elif guess(mid) == 0:
                return mid
            print(mid)
    
def guess(n, pick=1):
    if pick < n :
        return - 1
    elif pick > n:
        return 1

    else:
        return 0

sol = Solution()
n = 2
pick = 1
print(sol.guessNumber(n))
