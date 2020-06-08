"""
Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.
"""

import unittest

# graph node class


class Node:
    def __init__(self, value):
        self.value = value

        self.left = None
        self.right = None

# creating BST from array


class MakeTree:
    # constructor
    def __init__(self):
        pass

    def minimal_tree(self, array):

        return self.makeTree(array)

    def makeTree(self, array):  # Binary search Tree from array, inorder traversal

        if len(array) == 1:
            return Node(array[0])

        elif not array:  # even number of elements in an array
            return None

        mid = len(array) // 2

        root = Node(array[mid])

        root.left = self.makeTree(array[:mid])

        root.right = self.makeTree(array[mid + 1:])

        return root


# Tree serializer into inorder


class TreeSerializer:

    def __init__(self):
        self.ans = []

    def inorder(self, root):
        if not root:
            return self.ans  # if an empty tree return empty array

        self.inorder(root.left)

        self.ans.append(root.value)

        self.inorder(root.right)

        return self.ans


# write Test


class TestBST(unittest.TestCase):

    def test_bst_serializer(self):

        minTree = MakeTree()
        input_arr = [1, 2]

        root = minTree.minimal_tree(input_arr)

        inorderArr = TreeSerializer()
        self.assertEqual(inorderArr.inorder(root), input_arr)


# it means if we run this script then the below code will execute
# but if we import this module the below code will get skipped
if __name__ == '__main__':

    unittest.main()

"""
Runtime Analysis:
MakeTree.makeTree() takes an array and returns inorder tree. 
To make it, it required O(n) time complexity and O(n) space-complexity

To reverse the process:
TreeSerializer.inorder() takes the root and returns the serialized inorder array.
To make it, it required O(n) time complexity and O(n) space complexity.
"""
