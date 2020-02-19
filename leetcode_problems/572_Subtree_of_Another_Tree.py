"""
 Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2

Given tree t:

   4 
  / \
 1   2

Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0

Given tree t:

   4
  / \
 1   2
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSubtree(self, s, t):
        string_s = self.traverse_tree(s)
        string_t = self.traverse_tree(t)

        if string_t in string_s:
            return True
        else:
            False

    def traverse_tree(self, root):
        if not root:
            return
        # "#" used as delimeter between nodes
        return "#{}{}{}".format(root.val, self.traverse_tree(root.left), self.traverse_tree(root.right))


"""
references:
https://leetcode.com/problems/subtree-of-another-tree/discuss/386209/Python-98-speed-with-comments

corner case:
[12]
[2]

"""
