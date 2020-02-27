"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than or equal to the node's key.
    The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
    Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root):
        # Solution 1: iterative
        # if not root:
        #     return []
        # stack = [root]
        # dic = {}

        # while stack:  # O(n)
        #     node = stack.pop()
        #     dic[node.val] = dic.get(node.val, 0)+1

        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)

        # max_val = max(dic.values())
        # l = [k for k, v in dic.items() if v == max_val]

        # # l.sort()  # O(nlogn), if question ask to return in increasing order of values
        # # print(l)
        # return l

        # Solution 2: recursive
        #     if not root:
        #         return []
        #     self.dic = {}
        #     self.inorder(root)
        #     max_val = max(self.dic.values())
        #     return [k for k, v in self.dic.items() if v == max_val]

        # def inorder(self, root):
        #     if not root:
        #         return

        #     self.inorder(root.left)
        #     self.dic[root.val] = self.dic.get(root.val, 0)+1

        #     self.inorder(root.right)

        # Solution 3: recursive, fastest

        if not root:
            return []

        self.current_count = 0
        self.max_count = 0
        self.result = []
        self.prev = 0

        self.inorder(root)

        return self.result

    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)

        if root.val == self.prev:
            self.current_count += 1
        else:
            self.current_count = 1

        if self.current_count > self.max_count:
            self.result = [root.val]
            self.max_count = self.current_count

        elif self.current_count == self.max_count:
            self.result.append(root.val)

        self.prev = root.val

        self.inorder(root.right)


"""
reference:
https://leetcode.com/problems/find-mode-in-binary-search-tree/discuss/406028/Python-inorder-traversal-O(1)-space-with-explanation
"""
