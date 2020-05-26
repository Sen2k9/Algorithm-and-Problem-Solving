"""
Given an array arr of positive integers, consider all binary trees such that:

    Each node has either 0 or 2 children;
    The values of arr correspond to the values of each leaf in an in-order traversal of the tree.  (Recall that a node is a leaf if and only if it has 0 children.)
    The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.

Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit integer.

Example 1:

Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4

Constraints:

    2 <= arr.length <= 40
    1 <= arr[i] <= 15
    It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is less than 2^31).

"""


class Solution:
    def mctFromLeafValues(self, arr):
        # Solution : optimized, monotonic stack
        # Solution for the given problem, O(n)

        # stack = [float("Inf")]
        # ans = 0

        # for num in arr:

        #     while stack and stack[-1] <= num:
        #         curr = stack.pop()

        #         ans += curr * min(stack[-1], num)

        #     stack.append(num)

        # while len(stack) > 2:  # if all numbers are given in descending order
        #     ans += stack.pop()*stack[-1]

        # return ans

        # Solution for my problem given below, O(n)

        stack = [-float('inf')]

        ans = 0

        for num in arr:

            while stack and stack[-1] >= num:
                curr = stack.pop()

                ans += curr * max(stack[-1], num)

            stack.append(num)

        while len(stack) > 2:
            ans += stack.pop() * stack[-1]

        return ans


sol = Solution()
#arr = [9, 2, 4, 5, 8]
#arr = [9, 8, 7, 6, 5, 4]
arr = [1, 2, 3, 4, 5]
print(sol.mctFromLeafValues(arr))


"""
any kind of order (in-order, pre-order, post-order) works same for this problem

try the same problem given the condition below

    Each node has either 0 or 2 children;
    The values of arr correspond to the values of each leaf in an in-order traversal of the tree.  (Recall that a node is a leaf if and only if it has 0 children.)
    The value of each non-leaf node is equal to the product of the smallest leaf value in its left and right subtree respectively.
Among all possible binary trees considered, return the largest possible sum of the values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit integer.
"""
