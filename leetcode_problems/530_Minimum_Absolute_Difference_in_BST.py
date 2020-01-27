"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode):
        # Solution 1: self
        #     self.l = []
        #     self.helper(root)
        #     m = float("inf")
        #     for i in range(len(self.l)-1):
        #         if abs(self.l[i] - self.l[i+1]) < m:
        #             m = abs(self.l[i]-self.l[i+1])
        #     return m

        # def helper(self, root):
        #     if not root:
        #         return

        #     self.helper(root.left)
        #     self.l.append(root.val)
        #     self.helper(root.right)

        # Solution 2: faster and clean

        return self.helper(root, -float("Inf"), float("Inf"))

    def helper(self, root, lo, hi):
        if not root:
            return hi-lo

        left = self.helper(root.left, lo, root.val)
        right = self.helper(root.right, root.val, hi)

        return min(left, right)


"""
reference:
https://leetcode.com/problems/minimum-absolute-difference-in-bst/discuss/338515/Python-recursive
"""
