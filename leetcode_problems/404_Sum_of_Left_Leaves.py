"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode):
        # Solution 1: self, faster
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        queue = []
        queue.append(root)
        total = 0

        while queue:
            node = queue.pop(0)
            if not node.left and not node.right:
                total += node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                if not node.right.left and not node.right.right:
                    continue
                else:
                    queue.append(node.right)
        return total


"""
corner case:
1. single node [1]
"""
