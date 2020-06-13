"""
Check Subtree:
T1 and T2 are two very large binary trees, with T1 much bigger than T2.
Create an algorithm to determine if T2 is a subtree of T1.
A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.
"""


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None

        self.right = None


class BST:

    def __init__(self):
        pass

    def makeTree(self, arr):
        if not arr:
            return None

        elif len(arr) == 1:
            return Node(arr[0])

        mid = len(arr) // 2

        root = Node(arr[mid])
        left = self.makeTree(arr[:mid])
        root.left = left

        right = self.makeTree(arr[mid + 1:])
        root.right = right

        return root


class Serialize:

    def __init__(self):
        pass

    def bstSerialize(self, root, arr):

        if not root:
            return

        self.bstSerialize(root.left, arr)
        arr.append(root.val)

        self.bstSerialize(root.right, arr)
        return arr


class CheckSubtree:

    def __init__(self):
        pass

    def checkSubtree(self, root1, root2):

        if not root2:
            return True

        import pdb
        # pdb.set_trace()
        for node in self.tree_generator(root1):
            if node.val == root2.val:

                # print("here")
                if self.match(node, root2):
                    return True

        return False

    def tree_generator(self, root):
        if not root:
            return

        yield root

        for node in self.tree_generator(root.left):
            yield node

        for node in self.tree_generator(root.right):
            yield node

    def match(self, root1, root2):
        if not root1:
            if not root2:

                return True

            else:
                return False

        if not root2:
            return False

        if root1.val != root2.val:
            return False

        return self.match(root1.left, root2.left) and self.match(root1.right, root2.right)


if __name__ == '__main__':
    bst = BST()
    root1 = bst.makeTree([1, 2, 3, 4, 5, 6, 7])

    serial = Serialize()

    print(serial.bstSerialize(root1, []))

    bst = BST()
    root2 = bst.makeTree([1, 2, 3, 4, 5, 6])

    serial2 = Serialize()

    print(serial2.bstSerialize(root2, []))

    sol = CheckSubtree()
    print(sol.checkSubtree(root1, root2))


"""
very efficient solution:
https://github.com/w-hat/ctci-solutions/blob/master/ch-04-trees-and-graphs/10-is-subtree.py
"""
