"""
check balanced:
Implement a function to check if a binary tree is balanced. For the purposes of this question,
a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never
differ by more than one.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        pass

    def makeTree(self, array):
        if not array:
            return []

        if len(array) == 1:
            return Node(array[0])

        mid = len(array) // 2

        root = Node(array[mid])
        root.left = self.makeTree(array[:mid])
        root.right = self.makeTree(array[mid + 1:])

        return root


class Solution:

    def __init__(self):
        pass

    def check_balanced_bst(self, root):
        return self.check_balanced(root) != -1

    def check_balanced(self, root):

        if not root:
            return 0

        left = self.check_balanced(root.left)

        right = self.check_balanced(root.right)
        #print(left, right)

        if abs(left - right) > 1 or left == -1 or right == -1:
            return -1

        return max(left, right)+1


if __name__ == '__main__':

    bst = BST()

    sol = Solution()
    root = bst.makeTree([1, 2, 3, 4, 5, 6, 7])

    assert sol.check_balanced_bst(root) == True
    root = bst.makeTree([1, 2, 3, 4, 5, 6])

    assert sol.check_balanced_bst(root) == True
    root = bst.makeTree([1])

    assert sol.check_balanced_bst(root) == True
    root = bst.makeTree([])

    assert sol.check_balanced_bst(root) == True
