"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int):
        # Solution 1: clean, iterative

        if not root:
            return False
        queue = [(root, 0)]

        while queue:
            node, total = queue.pop()
            total = total + node.val

            if total == sum and not node.left and not node.right:
                return True

            if node.right:
                queue.append((node.right, total))
            if node.left:
                queue.append((node.left, total))

        return False

        # Solution 2: recursive

        def calculate(node, total):
            if not node:
                return False

            if not node.left and not node.right:
                total = total + node.val
                if total == sum:
                    return True

            return calculate(node.left, total+node.val) or calculate(node.right, total+node.val)

        return calculate(root, 0)

        # Solution 3: clean, recursion
        if not root:
            return False

        sum -= root.val

        if sum == 0 and not root.left and not root.right:
            return True

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

        # Solution 4: clean, iterative
        # iterative
        if not root:
            return False

        queue = []

        queue.append([root, sum])

        while queue:

            node, sum = queue.pop()

            sum -= node.val

            if sum == 0 and not node.left and not node.right:
                return True
            if node.right:
                queue.append([node.right, sum])

            if node.left:
                queue.append([node.left, sum])

        return False


"""
reference:
https://leetcode.com/problems/path-sum/discuss/366622/Python-recursive-and-iterative-using-pre-order
"""
