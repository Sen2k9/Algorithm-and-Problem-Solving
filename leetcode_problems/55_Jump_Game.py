"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:

    1 <= nums.length <= 3 * 10^4
    0 <= nums[i][j] <= 10^5


"""


class Solution:
    def canJump(self, nums) -> bool:
    #     self.memo = [0] * len(nums)
    #     self.memo[len(nums)-1] = 1
    #     return self.canJumpfrom(0, nums)

    # def canJumpfrom(self, position, nums):
    #     if self.memo[position] != 0:
    #         if self.memo[position] == -1:
    #             return False
    #         else:
    #             return True
        
    #     #print(self.memo)
    #     furthest_move = min(position + nums[position], len(nums) - 1)
    #     #print(position, furthest_move)

    #     for nextPosition in range(position + 1, furthest_move + 1):
    #         if self.canJumpfrom(nextPosition, nums):
    #             self.memo[position] = 1

    #             return True
        
    #     self.memo[position] = -1
    #     return False
    
        # optimal solution O(n), O(1)

        last_jump = len(nums) - 1

        for position in range(len(nums) - 2, -1, -1):

            if position + nums[position] >= last_jump:
                last_jump = position

        return last_jump == 0



sol = Solution()
nums = [3,2,1,0,4]
print(sol.canJump(nums))

nums = [2,3,1,1,4]
print(sol.canJump(nums))

nums = [2]
print(sol.canJump(nums))

nums = [0, 0]
print(sol.canJump(nums))