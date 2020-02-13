"""
Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:

Input: 
         1
       /   \
      2     3
Output: 1
Explanation: 
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1

Note:

    The sum of node values in any subtree won't exceed the range of 32-bit integer.
    All the tilt values won't exceed the range of 32-bit integer.
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTilt(self, root: TreeNode):
        if not root:
            return 0
        left_tilt = 0
        right_tilt = 0
        left_sum = 0
        right_sum = 0

        if root.left:
            left_tilt, left_sum = self.helper(root.left, 0, 0, 0, 0, 0)
            print(left_sum)

        if root.right:
            right_tilt, right_sum = self.helper(root.right, 0, 0, 0, 0, 0)
            print(right_sum)

        return left_tilt+right_tilt+abs(left_sum-right_sum)

    def helper(self, root, total, left_tilt, right_tilt, left_sum, right_sum):

        _left_tilt = 0
        _right_tilt = 0
        _left_sum = 0
        _right_sum = 0
        if root.left:
            _left_tilt, _left_sum = self.helper(
                root.left, total, left_tilt, right_tilt, left_sum, right_sum)

        if root.right:
            _right_tilt, _right_sum = self.helper(
                root.right, total, left_tilt, right_tilt, left_sum, right_sum)

        total = _left_sum+_right_sum

        return _left_tilt+_right_tilt+abs(_left_sum-_right_sum), total+root.val
