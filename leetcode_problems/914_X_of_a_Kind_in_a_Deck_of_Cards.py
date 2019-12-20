"""
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

    Each group has exactly X cards.
    All the cards in each group have the same integer.

 

Example 1:

Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]

Example 2:

Input: [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.

Example 3:

Input: [1]
Output: false
Explanation: No possible partition.

Example 4:

Input: [1,1]
Output: true
Explanation: Possible partition [1,1]

Example 5:

Input: [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2]


Note:

    1 <= deck.length <= 10000
    0 <= deck[i] < 10000

"""


class Solution:
    def hasGroupsSizeX(self, deck):
        # Optimum solution 1: using gcd
        from math import gcd
        from collections import Counter
        if len(deck) < 2:
            return False
        values = set(Counter(deck).values())
        gcd_val = next(iter(values))
        for each in values:
            gcd_val = gcd(gcd_val, each)
            if gcd_val == 1:
                return False
        return True


sol = Solution()
deck = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]
print(sol.hasGroupsSizeX(deck))
"""
corner case:
1. at least 2 elements
2. two groups with same elements
"""
