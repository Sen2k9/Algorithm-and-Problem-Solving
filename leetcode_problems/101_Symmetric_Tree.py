"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root):
        # Solution 1: self, iterative
        # if not root:
        #     return True
        # queue = []
        # queue.append(root)

        # level_order = []

        # while queue:
        #     for i in range(len(queue)):

        #         node = queue.pop(0)
        #         if node.left:
        #             level_order.append(node.left.val)
        #             queue.append(node.left)
        #         else:
        #             level_order.append('X')

        #         if node.right:
        #             level_order.append(node.right.val)
        #             queue.append(node.right)
        #         else:
        #             level_order.append('X')

        #     i = 0
        #     j = len(level_order) - 1
        #     # print(level_order)
        #     while i <= j:
        #         if level_order[i] != level_order[j]:
        #             return False
        #         else:
        #             level_order.pop(0)
        #             level_order.pop(-1)
        #             i = 0
        #             j = len(level_order)-1
        # return True

        # Solution 2: recursion
        # if not root:
        #     return True

        # def check(t1, t2):
        #     if not t1 and not t2:
        #         return True
        #     if t1 and not t2:
        #         return False
        #     elif not t1 and t2:
        #         return False
        #     elif t1.val != t2.val:
        #         return False
        #     #print(t1.val, t2.val)

        #     return check(t1.left, t2.right) and check(t1.right, t2.left)

        # return check(root.left, root.right)

        # Solution 3:

        if not root:
            return True

        if not root.left and not root.right:
            return True

        stack = [(root.left, root.right)]
        while stack:
            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue

            if not node1 or not node2:
                return node1 == node2

            if node1.val != node2.val:
                return False

            stack.append((node1.right, node2.left))
            stack.append((node1.left, node2.right))
        return True
        # reference : https://leetcode.com/problems/symmetric-tree/discuss/418810/Using-binary-same-tree-approach-python-stack-solution
