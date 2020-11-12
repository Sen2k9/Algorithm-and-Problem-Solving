"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations. [1,2,1] is not valid because 1 is used twice.
Example 4:

Input: k = 3, n = 2
Output: []
Explanation: There are no valid combinations.
Example 5:

Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
Explanation:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
​​​​​​​There are no other valid combinations.

Constraints:

2 <= k <= 9
1 <= n <= 60
"""
from collections import deque

class Solution:
    def combinationSum3(self, k: int, n: int):
        # result = []
        # def backtracking(remaining, combo_list, next_number):

        #     if remaining == 0 and len(combo_list) == k:

        #         # although combo_list is a list we need to cast it to list(combo_list)
        #         # because list keeps the reference, casting it to list type will remove the reference from the original
        #         # and will create a new list reference which will be saved in the result list
        #         # if we don not cast it to list, as at the end of the backtracking function we are popping out every element
        #         # the result will have three empty list inside of it, because every inner list has same reference for combo_list
        #         # and we popping out every element from the same reference at the end
        #         # this is a very pythonic way problem
        #         result.append(combo_list)
        #         print(result)
        #         return

        #     elif remaining < 0 or len(combo_list) > k:
        #         return

        #     for i in range(next_number, 9):
        #         combo_list.append(i + 1)
        #         backtracking(remaining - i - 1, combo_list, i + 1)

        #         # go to next choice

        #         #combo_list.pop()

        # backtracking(n, [], 0)

        # return result
        # using dfs

        result = []

        queue = deque()
        queue.append([9,[],0])

        size = 0
        while queue:

            remaining, combo_list, next_number = queue.popleft()

            # keep track of queue size
            if len(queue) > size:
                size = len(queue)
            
            if len(combo_list) == k and remaining == 0:
                result.append(combo_list)

            elif remaining < 0 or len(combo_list) > k:
                continue

            for i in range(next_number, n):

                queue.append([remaining - i - 1, combo_list + [i+1], i + 1])

            #print(queue)

        return result, size



sol = Solution()
k = 3
n = 9

print(sol.combinationSum3(k,n))