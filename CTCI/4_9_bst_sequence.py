"""
BST Sequence:
A binary search tree was created by traversing through an array from left to right and inserting each element.
Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# create a bst


class BST:

    def __init__(self):
        pass

    def makeBST(self, array):

        root = Node(array[0])

        for each in array[1:]:
            self.addNode(root, Node(each))

        return root

    def addNode(self, root, node):

        if node.value <= root.value:
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


# converting back to array


def serialize(root, array):

    if not root:
        return

    array.append(root.value)

    serialize(root.left, array)
    serialize(root.right, array)


class Solution:

    def __init__(self):
        pass

    def weaveList(self, first, second, result, prefix):

        if not first or not second:
            result.append(prefix + first + second)
            return result

        firstHead, firstTail = first[0], first[1:]

        self.weaveList(firstTail, second, result, prefix+[firstHead])

        secondHead, secondTail = second[0], second[1:]
        self.weaveList(first, secondTail, result, prefix+[secondHead])

    def allSequences(self, root):

        if not root:
            return []

        answer = []

        prefix = [root.value]

        # return all the sequences from left subtree
        left = self.allSequences(root.left) or [[]]

        # return all the sequences from right subtree
        right = self.allSequences(root.right) or [[]]

        for left_index in range(len(left)):
            for right_index in range(len(right)):

                weave = []

                self.weaveList(left[left_index],
                               right[right_index], weave, prefix)

            answer.extend(weave)  # extend or merge the two iterable
            # print(answer)

        return answer


if __name__ == '__main__':
    bst = BST()
    # create binary search tree from the array taking input from left to right
    root = bst.makeBST([2, 1, 3, 4, 5, 6])

    array = []
    # not necessary for this problem, just to make sure the serialization works
    serialize(root, array)
    # print(array)

    sol = Solution()
    # create and print all sequence of array possible to create the make binary search tree
    for seqN, seqList in enumerate(sol.allSequences(root)):
        print(f"{seqN:03}:{seqList}")


"""
refences: 
https://stackoverflow.com/questions/21211701/given-a-bst-and-its-root-print-all-sequences-of-nodes-which-give-rise-to-the-sa
"""
