"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5

Output: 2

 

Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5

Output: 2

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestUnivaluePath(self, root):
        self.longest = 0
        self.unipath(root)
        return self.longest

    def unipath(self, root):
        if not root:
            return None, 0

        if not root.left and not root.right:
            return root.val, 1

        left, count_l = self.unipath(root.left)
        right, count_r = self.unipath(root.right)

        if left == root.val and right == root.val:
            self.longest = max(self.longest, count_l + count_r)
            return root.val, max(count_l, count_r)+1

        elif left == root.val:
            self.longest = max(self.longest, count_l)
            return root.val, count_l + 1

        elif right == root.val:
            self.longest = max(self.longest, count_r)
            return root.val, count_r + 1

        return root.val, 1


"""
reference:
https://leetcode.com/problems/longest-univalue-path/discuss/316124/Python-Recursive-Solution-DFS-Easy-To-Understand
"""
