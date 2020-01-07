"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

 

Note:

    The number of nodes in the tree will be between 2 and 100.
    Each node has a unique integer value from 1 to 100.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isCousins(self, root, x, y):
        #g_depth = 0
        #g_parent = 0

        def dfs(root, val, depth, parent):
            if not root:
                return
            if root.val == val:
                global g_depth
                global g_parent
                g_depth = depth
                g_parent = parent
                return

            else:
                dfs(root.left, val, depth + 1, root.val)
                dfs(root.right, val, depth+1, root.val)

        dfs(root, x, 0, 0)
        x_depth = g_depth
        x_parent = g_parent
        dfs(root, y, 0, 0)
        y_depth = g_depth
        y_parent = g_parent

        return x_depth == y_depth and x_parent != y_parent


"""
reference:
https://leetcode.com/problems/cousins-in-binary-tree/discuss/462369/Python-DFS-solution-beats-100-time-and-100-memory
"""
