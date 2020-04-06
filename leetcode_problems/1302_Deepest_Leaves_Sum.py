"""
Given a binary tree, return the sum of values of its deepest leaves.

Example 1:

Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Constraints:

    The number of nodes in the tree is between 1 and 10^4.
    The value of nodes is between 1 and 100.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def deepestLeavesSum(self, root: TreeNode):
        from collections import deque
        queue = deque()
        queue.append(root)

        while queue:
            n = len(queue)
            node_sum = 0

            for _ in range(n):
                node = queue.popleft()

                node_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
        return node_sum
