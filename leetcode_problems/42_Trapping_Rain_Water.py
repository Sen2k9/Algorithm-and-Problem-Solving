"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6


"""


class Solution:
    def trap(self, height) -> int:
        # brute-force solution Time: O(n^2)
        # if len(height) < 3:
        #     return 0
        # total_water = 0

        # for i in range(1, len(height)- 1):

        #     left_max = max(height[0: i])
        #     right_max = max(height[i + 1 :])

        #     eligible_height = min(left_max, right_max)

        #     if not eligible_height:
        #         continue

        #     trapped_water = eligible_height - height[i]

        #     if trapped_water <= 0:
        #         continue

        #     total_water += trapped_water

        # return total_water

        # Dynamic Programming Solution: Time O(n), Space O(n)
        if not height:
            return 0
        left_max = [0]*len(height)
        right_max = [0] * len(height)

        length = len(height)
        left_max[0] = height[0]

        for i in range(1, len(height)):
            left_max[i] = max(height[i], left_max[i - 1])

        right_max[length-1] = height[length-1]

        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        print(left_max, right_max)

        total_water = 0

        for i in range(1, len(height)):
            total_water += min(left_max[i], right_max[i]) - height[i]

        return total_water






sol = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(height))

height = [1, 0, 2]
print(sol.trap(height))

height = [0, 1, 2]
print(sol.trap(height))

height = [2, 1, 0]
print(sol.trap(height))

height = [2, 1]
print(sol.trap(height))