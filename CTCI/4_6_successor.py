"""
Successor:
Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree.
You may assume that each node has a link to the parent.
"""

# node class


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# make BST


class BST:

    def __init__(self):
        pass

    def makeBST(self, array):

        if not array:  # for empty array
            return []

        if len(array) == 1:  # base case

            return Node(array[0])

        mid = len(array) // 2
        root = Node(array[mid])  # middle element, root of the tree

        root.left = self.makeBST(array[:mid])  # left half
        root.right = self.makeBST(array[mid + 1:])  # right half

        return root

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        if p == root:
            return self.leftMostChild(p.right) if p.right else None

        return self.helper(root, p, None, None)

    def helper(self, root, p, minNode, maxNode):
        if not root:
            return

        if root == p:
            if p.right:
                return self.leftMostChild(p.right)

            else:

                if maxNode:
                    return maxNode
                else:
                    return None

        leftFound = self.helper(root.left, p, minNode, root)
        if leftFound:
            return leftFound

        rightFound = self.helper(root.right, p, root, maxNode)

        if rightFound:
            return rightFound

    def leftMostChild(self, root):
        if not root.left:
            return root

        return self.leftMostChild(root.left)


"""

                 10
               /    \                   
              3      20 
            /   \    /  \
           1     4   15  22
                  \  /     \
                  9  11     25

         9, 10, 25

Same as Leetcode 285.Inorder_Successor_in_BST. See the question there for better understanding and see the answer in CTCI 4.6
"""
