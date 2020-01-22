"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode):
        # Solution 1: self, recursion
        if not p and not q:
            return True
        elif not p or not q:
            return False

        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # Solution 1: self, iterative
        if not p and not q:
            return True
        queue = [(p, q)]
        while queue:
            n1, n2 = queue.pop()
            if not n1 and not n2:
                continue
            elif not n1 or not n2:
                return False

            if n1.val != n2.val:
                return False

            if n1.left or n2.left:
                queue.append((n1.left, n2.left))

            if n1.right or n2.right:
                queue.append((n1.right, n2.right))
        return True
