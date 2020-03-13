"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int):
        #     self.result = [0, False]
        #     self.node_count = 0

        #     self.helper(root, k)

        #     return self.result[0]

        # def helper(self, root, k):
        #     if not root:
        #         return

        #     if self.result[1] == False:
        #         self.helper(root.left, k)

        #     self.node_count += 1

        #     if self.node_count == k:
        #         self.result[0] = root.val
        #         self.result[1] = True
        #         return

        #     if self.result[1] == False:
        #         self.helper(root.right, k)

        # Solution 2: iterative

        result = []
        queue = [[root, False]]
        count = 0

        while queue:
            node, visited = queue[-1]

            if not node.left and not node.right:
                result.append(queue.pop())
                count += 1
                if count == k:
                    return node.val
                continue

            if node.left:
                if not visited:
                    queue[-1][1] = True
                    queue.append([node.left, False])
                    continue
                else:
                    result.append(queue.pop())
                    count += 1
                    if count == k:
                        return node.val

            if node.right:
                queue.append([node.right, False])
