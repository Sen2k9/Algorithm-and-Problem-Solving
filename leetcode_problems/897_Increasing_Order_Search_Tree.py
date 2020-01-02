"""
Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9

Note:

    The number of nodes in the given tree will be between 1 and 100.
    Each node will have a unique integer value from 0 to 1000.

"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root: TreeNode):
        # Solution 1: self, works faster with large N
        # O(n)
        queue = []
        queue.append(root)
        result = []
        visited = {}

        node = queue[-1]
        visited[node] = True
        while node:

            if node.left is not None and visited.get(node.left, False) is False:
                queue.append(node.left)
                visited[node.left] = True
                node = node.left

            else:
                if node.left is None or visited.get(node.left, False) is True:

                    new_node = queue.pop()
                    if new_node.right:
                        queue.append(new_node.right)
                        visited[new_node.right] = True
                    new_node.left = None

                    result.append(new_node)

                    if len(result) > 1:
                        result[-2].right = result[-1]
                    if queue:
                        node = queue[-1]
                    else:
                        node = None
        return result[0]

        # Solution 2: using recursion
        # O(nlogn)
        # def in_order(node):
        #     if node is None:
        #         return []
        #     return in_order(node.left) + [node] + in_order(node.right)

        # nodelist = in_order(root)
        # for i in range(len(nodelist) - 1):
        #     nodelist[i].right = nodelist[i + 1]
        #     nodelist[i].left = None
        # nodelist[-1].left = None
        # nodelist[-1].right = None
        # return nodelist[0]


sol = Solution()
root = [5, 3, 6, 2, 4, null, 8, 1, null, null, null, 7, 9]
print(sol.increasingBST(root))
"""
corner case:
in-order traversal (LNR)
"""
