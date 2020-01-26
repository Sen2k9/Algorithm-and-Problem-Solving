"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root: TreeNode):
        # Solution 1: self,
        # Runtime : O(n), O(n)
        #     self.nodes = []
        #     self.values = []
        #     self.helper(root)

        #     for i in range(len(self.nodes)):
        #         node = self.nodes[i]
        #         node.val = node.val + sum(self.values[i+1:])

        #     return root

        # def helper(self, root):  # in-order traversal
        #     if not root:
        #         return

        #     self.helper(root.left)

        #     self.nodes.append(root)
        #     self.values.append(root.val)

        #     self.helper(root.right)

        # Soltuion 2; clean and efficient

        self.sum = 0
        return self.reverse_inOrder(root)

    def reverse_inOrder(self, root):
        if not root:
            return

        self.reverse_inOrder(root.right)
        self.sum = self.sum + root.val

        root.val = self.sum

        self.reverse_inOrder(root.left)

        return root
