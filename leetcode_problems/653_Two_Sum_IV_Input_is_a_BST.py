"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True

Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root: TreeNode, k: int):
        # Solution 1: self, recursive
        dic = {}
        if not root.left and not root.right:
            return False

        def helper(root, dic, k):
            if not root:
                return False

            a = (k-root.val) in dic

            dic[root.val] = True

            return a or helper(root.left, dic, k) or helper(root.right, dic, k)

        return helper(root, dic, k)

        # Solution 2: self, iterative, faster
        dic = {}
        from collections import deque
        queue = deque([root])

        while queue:

            for _ in range(len(queue)):
                node = queue.popleft()
                if k-node.val in dic:
                    return True
                else:
                    dic[node.val] = True

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return False

        # Solution 3: using set, fastest
        dic = set()
        from collections import deque
        queue = deque([root])

        while queue:

            for _ in range(len(queue)):
                node = queue.popleft()
                if k-node.val in dic:
                    return True
                else:
                    dic.add(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return False
