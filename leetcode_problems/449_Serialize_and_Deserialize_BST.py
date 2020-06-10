"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# create a bst


class BST:

    def __init__(self):
        pass

    def makeBST(self, array):

        root = TreeNode(array[0])

        for each in array[1:]:
            self.addNode(root, TreeNode(each))

        return root

    def addNode(self, root, node):

        if node.val <= root.val:
            if not root.left:
                root.left = node
                return

            else:
                return self.addNode(root.left, node)

        else:

            if not root.right:
                root.right = node
                return

            else:
                return self.addNode(root.right, node)


class Codec:

    def serialize(self, root: TreeNode):  # can not use any extra variable
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        #array = []

        # "|" seprates the node in case the have two or more degits
        return "|".join(map(str, self.preorder(root)))

    def preorder(self, root):  # pre-order travarsal

        if not root:
            return []

        return [root.val] + self.preorder(root.left) + self.preorder(root.right)

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        array = data.split("|")  # split the string
        print(array)

        root = TreeNode(int(array[0]))

        for each in array[1:]:
            self.addNode(root, TreeNode(int(each)))

        return root

    def addNode(self, root, node):

        if node.val <= root.val:
            if not root.left:
                root.left = node

            else:
                self.addNode(root.left, node)

        else:

            if not root.right:
                root.right = node

            else:
                self.addNode(root.right, node)


if __name__ == '__main__':

    codec = Codec()

    bst = BST()
    root = bst.makeBST([10, 1, 29, 3, 5, 6, 7])
    print(codec.serialize(root))

    print(codec.deserialize(codec.serialize(root)))
