"""
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows.

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.

Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
"""


class Solution:
    def getHint(self, secret, guess):
        # Solution 1: optimized, fastest
        from collections import Counter

        new_secret = ""
        new_guess = ""
        A = 0
        B = 0

        for i in range(len(secret)):
            if secret[i] != guess[i]:
                new_secret += secret[i]
                new_guess += guess[i]
            else:
                A += 1
        count_sec = Counter(new_secret)
        count_guess = Counter(new_guess)

        for k, v in count_guess.items():
            B += min(v, count_sec.get(k, 0))

        return "{}A{}B".format(A, B)


sol = Solution()
secret = "11"
guess = "01"
print(sol.getHint(secret, guess))
"""
corner case:
"11"
"10"

"11"
"01"

reference:
https://leetcode.com/problems/bulls-and-cows/discuss/453529/Python-fast-and-efficient-way-99-time-100-space

"""
