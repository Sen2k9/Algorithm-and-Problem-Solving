"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        from collections import defaultdict
        dic = defaultdict(int)
        curr_sum = 0
        stack = [(root, curr_sum, False)]
        path = 0
        while stack:
            node, curr_sum, backtrack = stack.pop()
            if backtrack:
                dic[curr_sum] -= 1
                continue
            curr_sum += node.val
            path += dic[curr_sum - node.val]
            dic[curr_sum] += 1
            stack.append((None, curr_sum, True))

            if node.left:
                stack.append((node.left, curr_sum, False))
            if node.right:
                stack.append((node.right, curr_sum, False))
        return path
