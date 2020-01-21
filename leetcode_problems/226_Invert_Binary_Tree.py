"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:

    Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode):
        # Solution 1: recursion
        # if not root:
        #     return None

        # r = self.invertTree(root.right)
        # l = self.invertTree(root.left)

        # root.right = l
        # root.left = r
        # return root

        # Solution 2: iterative
        from collections import deque

        if not root:
            return None

        queue = deque([root])

        while queue:
            curr = queue.popleft()
            temp = curr.right
            curr.right = curr.left
            curr.left = temp

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return root



"""
reference:
https://leetcode.com/problems/invert-binary-tree/discuss/360867/Python3-recursively-and-iteratively
"""
