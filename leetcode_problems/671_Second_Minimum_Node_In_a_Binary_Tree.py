"""
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.

Example 2:

Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root: TreeNode):
        # O(nlogn)
        values = {root.val}
        stack = [root]
        while stack:  # O(n)
            node = stack.pop()
            values.add(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        l = list(values)
        print(l)
        l.sort()  # O(nlogn)
        return l[1] if len(l) > 1 else - 1

        # Solution 2: recursive
        l = set(self.inordertraversal(root))  # O(n)
        if len(l) > 1:
            return sorted(list(l))[1]  # O(nlogn)
        else:
            return -1

    def inordertraversal(self, root):
        if not root:
            return []
        else:
            # L+N+R
            return self.inordertraversal(root.left) + [root.val] + self.inordertraversal(root.right)
