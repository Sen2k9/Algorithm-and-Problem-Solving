"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode):
        # # Solution 1: self, recursive

        # def paths(root, l):
        #     if not root:
        #         return None
        #     if not root.left and not root.right:
        #         return [str(root.val)]

        #     l_path = paths(root.left, [])

        #     r_path = paths(root.right, [])
        #     # print(l_path)
        #     # print(r_path)

        #     if l_path:
        #         for each in l_path:
        #             temp = str(root.val)+"->"+each
        #             l.append(temp)

        #     if r_path:
        #         for each in r_path:
        #             temp = str(root.val)+"->"+each
        #             l.append(temp)

        #     return l

        # if not root:
        #     return []
        # l = []

        # return paths(root, l)

        # Solution 2: faster

        def paths(root, path):
            if not root:
                return

            if not root.left and not root.right:
                self.result.append(path+str(root.val))
                return

            path = path + str(root.val)+"->"

            paths(root.left, path)

            paths(root.right, path)

        self.result = []
        path = ""

        paths(root, path)

        return self.result

        # Solution 3: iterative

        stack = []
        result = []
        stack.append((root, ""))

        while stack:
            node, path = stack.pop()

            if not node:
                continue

            if not node.left and not node.right:
                result.append("{}{}".format(path, node.val))

            stack.append((node.left, "{}{}->".format(path, node.val)))
            stack.append((node.right, "{}{}->".format(path, node.val)))

        return result


"""
reference:
https://leetcode.com/problems/binary-tree-paths/discuss/68441/Python-Easy-DFS-(Recursive-%2B-Iterative)-Solution
"""
