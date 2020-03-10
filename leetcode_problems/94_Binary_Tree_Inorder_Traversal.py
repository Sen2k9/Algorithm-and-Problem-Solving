"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode):
        # solution 1:
        # time : O(n)
        # space : O(n)
        #     self.result = []

        #     self.helper(root)
        #     return self.result

        # def helper(self, root):
        #     if not root:
        #         return

        #     self.helper(root.left)
        #     self.result.append(root.val)
        #     self.helper(root.right)

        # Solution 2: iterative
        #time : O(n)
        # space : O(n)
        if not root:
            return []
        result = []

        queue = [(root, False, False)]

        while queue:
            node, left_visited, right_visited = queue[-1]

            if not node.left and not node.right:
                result.append(node.val)
                queue.pop()
                continue

            if node.left and not left_visited:
                queue[-1] = (node, True, False)
                queue.append((node.left, False, False))
                continue
            else:
                result.append(node.val)
                queue.pop()
            if node.right:
                queue.append((node.right, False, False))
        return result

        # we can more optimize as right_visited has no use, we only need to keep track for left visited
