"""
We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

    If x == y, both stones are totally destroyed;
    If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

 

Note:

    1 <= stones.length <= 30
    1 <= stones[i] <= 1000

"""


class Solution:
    def lastStoneWeight(self, stones):
        # Solution 1: self
        # print(stones)
        # while len(stones) > 1:

        #     if len(set(stones)) == 1:
        #         if len(stones) % 2 == 0:
        #             return 0
        #         else:
        #             return stones[0]
        #     stones = sorted(stones)

        #     print(stones)
        #     val = stones[-1] - stones[-2]
        #     if val == 0:
        #         stones.pop(-1)
        #         stones.pop(-1)
        #     else:
        #         stones[-2] = val
        #         stones.pop(-1)

        # return stones[0]

        # Solution 2: Faster
        stones = sorted(stones)

        print(stones)
        while len(stones) > 1:

            y = stones.pop()
            x = stones.pop()

            if y-x == 0:
                continue
            else:
                stones.append(y - x)
                stones.sort()
            print(stones)

        if len(stones) == 1:
            return stones[0]
        else:
            return 0


sol = Solution()
stones = [2, 7, 4, 1, 8, 1]
print(sol.lastStoneWeight(stones))
"""
corner case:
1. all duplicate
2. one element

"""
