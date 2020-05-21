"""


You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

Example 1:

Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true

Example 2:

Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false

Example 3:

Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false

Example 4:

Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
Output: false

 

Constraints:

    1 <= n <= 10^4
    leftChild.length == rightChild.length == n
    -1 <= leftChild[i], rightChild[i] <= n - 1

"""

from collections import deque


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild, rightChild):
        # Solution 1:

        # if n == 1:
        #     return True

        # visited = set()

        # queue = deque()

        # for i in range(n):  # takes care of tree which does not starts with "0" 0<--1<--2<--3
        #     if i not in visited:

        #         queue.append(i)

        #         while queue:
        #             node = queue.popleft()

        #             if not leftChild[node] == -1:
        #                 queue.append(leftChild[node])

        #                 if leftChild[node] in visited:  # takes care of bidirectional edges
        #                     return False
        #                 else:
        #                     visited.add(leftChild[node])

        #             if not rightChild[node] == -1:

        #                 queue.append(rightChild[node])

        #                 # takes care of bidirectional edges
        #                 if rightChild[node] in visited:
        #                     return False
        #                 else:
        #                     visited.add(rightChild[node])

        # if len(visited) == n-1:  # takes care of not-connected nodes
        #     return True
        # else:
        #     return False
        """
        time complexity : O(n), outer for loop only executes when all the nodes are not-connected single node
        space complexity : O(n), visited set and queue store the node number

        """

        # Solution 2: faster
        if n == 1:
            return True
        queue = deque()

        for i in range(n):

            queue.append(i)
            visited = set()
            visited.add(i)

            while queue:

                node = queue.popleft()

                if not leftChild[node] == -1:
                    queue.append(leftChild[node])

                    if leftChild[node] in visited:
                        return False
                    else:
                        visited.add(leftChild[node])

                if not rightChild[node] == -1:
                    queue.append(rightChild[node])

                    if rightChild[node] in visited:
                        return False

                    else:
                        visited.add(rightChild[node])

            if len(visited) == n:  # we found a valid binary tree
                return True

        # after traversing all node if the below line executes, it means we haven't find any valid binary tree, some nodes are not-connected to make len(visited) == n

        return False


sol = Solution()
n = 2
leftChild = [1, -1]
rightChild = [-1, -1]
print(sol.validateBinaryTreeNodes(n, leftChild, rightChild))
"""
corner case:
1. check connected components
2. same child
2. bidirectional
"""
