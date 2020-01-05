"""
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

Note:

    1 <= costs.length <= 100
    It is guaranteed that costs.length is even.
    1 <= costs[i][0], costs[i][1] <= 1000
"""


class Solution:
    def twoCitySchedCost(self, costs):
        # Solution 1:
        # sorting costs by their cost differences

        costs = sorted(costs, key=lambda x: abs(x[0] - x[1]), reverse=True)
        # to make cost minimum, we need to select the minimum values first where the difference is largest and can make big change
        print(costs)
        city_a = len(costs) // 2
        city_b = city_a
        total = 0
        for _, val in enumerate(costs):
            if val[0] > val[1]:
                if city_b:
                    total += val[1]
                    city_b -= 1
                else:
                    total += val[0]
                    city_a -= 1

            else:
                if city_a:
                    total += val[0]
                    city_a -= 1
                else:
                    total += val[1]
                    city_b -= 1
        return total


sol = Solution()
costs = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
print(sol.twoCitySchedCost(costs))

"""
corner case:
1. duplicate is values

Algo:
to make cost minimum, we need to select the minimum values first where the difference is largest and can make big change

reference:
https://leetcode.com/problems/two-city-scheduling/discuss/278944/3-ways-to-solve.
https://leetcode.com/problems/two-city-scheduling/discuss/442268/Easy-Python-Solution%3A-Beats-99.03-100-less-memory

"""
