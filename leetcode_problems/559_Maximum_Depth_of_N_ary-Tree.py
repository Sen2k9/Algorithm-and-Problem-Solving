"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: 3

Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5

 

Constraints:

    The depth of the n-ary tree is less than or equal to 1000.
    The total number of nodes is between [0, 10^4].


"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root):
        # Solution 1: self
        # if not root:
        #     return 0
        # queue = [root]
        # dic = {}
        # dic[root] = 1
        # level = [dic[root]]
        # while queue:
        #     root = queue.pop()
        #     if root.children:
        #         for each in root.children:
        #             queue += [each]
        #             dic[each] = dic[root]+1

        #             level.append(dic[root] + 1)
        # # print(dic)
        # # print(level)
        # return max(level)

        # Solution 2: faster
        if not root:
            return 0

        depth = 1
        queue = []
        queue.append((root, 1))

        while queue:
            (node, d) = queue.pop()
            depth = max(depth, d)
            for each in node.children:
                queue.append((each, d + 1))
        return depth
