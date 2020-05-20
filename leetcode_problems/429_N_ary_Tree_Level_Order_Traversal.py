"""
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

 

Constraints:

    The height of the n-ary tree is less than or equal to 1000
    The total number of nodes is between [0, 10^4]


"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""




from collections import deque, OrderedDict
class Solution:

    def levelOrder(self, root):

        # Recursive
        if not root:
            return []

        self.level_nodes = OrderedDict()

        ans = []

        self.helper(root, level=0)

        for level, values in self.level_nodes.items():
            ans.append(values)

        return ans

    def helper(self, root, level):

        if level not in self.level_nodes:
            self.level_nodes[level] = [root.val]

        else:
            self.level_nodes[level].append(root.val)

        if root.children:
            for each in root.children:
                self.helper(each, level + 1)
