"""
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Note:

    Both of the given trees will have between 1 and 100 nodes.

"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode):
        # Solution 1: self, iterative, best
        # O(n+m)
        def leaf_nodes(node):
            arr = []
            result = []
            arr.append(node)
            while arr:
                root = arr.pop(0)
                if root.right:
                    arr = [root.right] + arr
                if root.left:
                    arr = [root.left] + arr

                if not root.left and not root.right:
                    result.append(root.val)

                # print(result)
            return result
        seq1 = leaf_nodes(root1)
        seq2 = leaf_nodes(root2)
        # if seq1 == seq2:
        #     return True
        # return False
        if len(seq1) != len(seq2):
            return False
        else:
            for i, val in enumerate(seq1):
                if val != seq2[i]:
                    return False
        return True

        # Solution 2: recursive, best for small input
        # O(nlogn + mlogn)
        def leaf_nodes(node, z):
            if not node:
                return
            elif not node.left and not node.right:
                z.append(node.val)
            else:
                leaf_nodes(node.left, z)
                leaf_nodes(node.right, z)

            return z
        x = []
        y = []

        one = leaf_nodes(root1, x)
        two = leaf_nodes(root2, y)

        return one == two


"""
corner case:
1. same length sequence but disordered
Input
[1,2,3]
[1,3,2]
"""
