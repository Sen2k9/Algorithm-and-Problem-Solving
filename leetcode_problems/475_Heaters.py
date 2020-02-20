"""
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:

    Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
    Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
    As long as a house is in the heaters' warm radius range, it can be warmed.
    All the heaters follow your radius standard and the warm radius will the same.

Example 1:

Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.

Example 2:

Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
"""


class Solution:
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        N = len(heaters)
        i = 0
        r = 0
        for house in houses:
            while i + 1 < N and heaters[i + 1] < house:
                i += 1
            r = max(r, min([abs(house - heat) for heat in heaters[i:i+2]]))
            # print(r)
        return r


sol = Solution()
houses = [1, 2, 3, 4, 5, 6, 7, 8, 9]
heaters = [2]
print(sol.findRadius(houses, heaters))

"""
references:
https://leetcode.com/problems/heaters/discuss/329868/Python-one-pass-through-'houses'
"""
