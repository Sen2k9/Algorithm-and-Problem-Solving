"""
Validate BST: Implement a function to check if a binary tree is a binary search tree
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

        elif len(array) == 1:
            return Node(array[0])

        mid = len(array) // 2

        root = Node(array[mid])

        root.left = self.makeTree(array[:mid])
        root.right = self.makeTree(array[mid + 1:])

        return root


class Solution:

    def __init__(self):
        pass

    def validate_bst(self, root):

        return self.helper(root, None, None)

    def helper(self, root, minNode, maxNode):
        if not root:
            return True

        if (minNode and root.value <= minNode) or (maxNode and root.value > maxNode):
            return False

        return self.helper(root.left, minNode, root.value) and self.helper(root.right, root.value, maxNode)


if __name__ == '__main__':

    bst = BST()

    sol = Solution()

    root = bst.makeTree([1, 2, 3, 4, 5, 6, 7])

    assert sol.validate_bst(root) == True

    root = bst.makeTree([1, 20, 3, 4, 5, 6, 7])

    assert sol.validate_bst(root) == False

    root = bst.makeTree([])

    assert sol.validate_bst(root) == True


"""
complexity analysis:
Runtime : O(n), as we search every node one by one
Space : O(logn), where logn is the height of the tree. This space is calulated based on the number of recursive call.
In this case, there are one recursive stack created for each recursive call
"""
