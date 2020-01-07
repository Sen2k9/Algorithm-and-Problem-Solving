"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

Example 1:

Input: [1,1,1,1,1,null,1]
Output: true

Example 2:

Input: [2,2,2,5,2]
Output: false

Note:

    The number of nodes in the given tree will be in the range [1, 100].
    Each node's value will be an integer in the range [0, 99].

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isUnivalTree(self, root):
        # Solution 1: self, iterative
        # queue = []
        # queue.append(root)
        # while queue:
        #     node = queue.pop()
        #     if node.left:
        #         queue.append(node.left)
        #         if node.left.val != node.val:
        #             return False
        #     if node.right:
        #         queue.append(node.right)
        #         if node.right.val != node.val:
        #             return False
        # return True
        # Solution 2: recursion

        # val = []

        # def dfs(node):
        #     if node:
        #         val.append(node.val)
        #     else:
        #         return
        #     dfs(node.left)
        #     dfs(node.right)

        # dfs(root)
        # return len(set(val)) == 1

        # Solution 3: recursion

        def uni(node):
            if not node:
                return

            if node.val != root.val:
                return False
            return uni(node.left) and uni(node.right)

        return uni(root)


sol = Solution()
print(sol.isUnivalTree)
