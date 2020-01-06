"""
Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.

Note:

    The size of the BST will be between 2 and 100.
    The BST is always valid, each node's value is an integer, and each node's value is different.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minDiffInBST(self, root):
        # Solution 1: self, fastest
        queue = []
        l = []
        queue.append(root)
        l.append(root.val)

        while queue:
            node = queue.pop()
            if node.left:
                l.append(node.left.val)

                queue.append(node.left)
            if node.right:
                l.append(node.right.val)
                queue.append(node.right)
        minm = float("Inf")
        l.sort()
        for i in range(len(l)-1):
            if abs(l[i]-l[i+1]) < minm:
                minm = abs(l[i]-l[i+1])
        return minm

        # Solution 2: recursive, slow
        # def fn(node, lo, hi):
        #     if not node:
        #         return hi - lo
        #     left = fn(node.left, lo, node.val)
        #     right = fn(node.right, node.val, hi)
        #     return min(left, right)
        # return fn(root, float('-inf'), float('inf'))
