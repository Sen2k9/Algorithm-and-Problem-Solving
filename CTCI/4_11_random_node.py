"""
Random Node:
You are implementing a binary tree class from scrath which, in addition to insert, find, and delete, has a method getRandomNode() which returns a random node from the tree.
All node should be equally likely to be chosen. Design and implement an algorithm to getRandomNode, and explain how you would implement the rest of the methods.
"""


class Node:

    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

        self.count = 1

        if self.left:
            self.count += self.left.count

        if self.right:
            self.count += self.right.count


class BST:

    def __init__(self):
        self.root = None

    def insert(self, val, root=None):

        if self.root:

            if val <= root:

                if not root.left:
                    root.left = Node(val)
                else:
                    return self.insert(val, root.left)

            else:

                if not root.right:
                    root.right = Node(val)

                else:

                    return self.insert(val, root.right)

        else:
            self.root = Node(val)

        return self.root

    def delete(self, node):

        root = self.find(self.root, node)

        root = None

    def find(self, root, node):

        if node == root:
            return node

        if node.val < root.val:
            return self.find(root.left, node)

        elif node.val > root.val:
            return self.find(root.right, node)

    def getRandam(self):
        import random

        return self.get_numbered_node(self.root, random.randint(1, self.root.count - 1))

    def get_numbered_node(self, root, number):

        if number == 1:
            return root

        if root.left:

            if number <= root.left.count:

                self.get_numbered_node(root.left, number - 1)

            else:

                self.get_numbered_node(root.right, number - root.left.count)

        if root.right:

            self.get_numbered_node(root.right, number-1)


if __name__ == '__main__':

    bst = BST()

    arr = [1, 2, 3, 4, 5, 6, 7]
