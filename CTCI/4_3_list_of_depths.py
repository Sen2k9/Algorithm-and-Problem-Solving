"""
List of Depths:
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth
(e.g., if you have a tree with depth D, you'll have D linked lists).
"""
# BST


from collections import deque


class BinarySearchTree:
    # constructor

    def __init__(self):
        pass

    def inorderTree(self, array):

        return self.makeTree(array)

    def makeTree(self, array):  # time O(logn), space O(logn)

        if not array:
            return None

        elif len(array) == 1:
            return Node(array[0])

        mid = len(array) // 2

        root = Node(array[mid])

        root.left = self.makeTree(array[:mid])
        root.right = self.makeTree(array[mid + 1:])

        return root


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class LinkedNode:

    def __init__(self, value):
        self.value = value
        self.next = None


# function convert bst to list of depth


def list_of_depth(root):
    if not root:
        return []
    ans = []

    queue = deque()

    queue.append(root)  # using a queue as extra

    while queue:
        length = len(queue)

        dummy = head = LinkedNode(0)
        for _ in range(length):
            node = queue.popleft()
            # print(node.value)

            head.next = LinkedNode(node.value)
            head = head.next

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        ans.append(dummy.next)

    return ans

# function convert list of depth to array again


def serializeList(array):

    ans = []

    for head in array:
        while head:
            ans.append(head.value)
            head = head.next

    return ans


# test your code
if __name__ == '__main__':

    bst = BinarySearchTree()
    array = []
    root = bst.inorderTree(array)

    answer = list_of_depth(root)  # array having linkedlist

    test_answer = serializeList(answer)
    #print(array, sorted(test_answer))

    assert array == sorted(test_answer)


"""
complexity analysis:

Runtime : O(n) for bfs, O(logn) for makeTree
Space : O(n) for using an extra queue for bfs, O(logn) for makeTree
"""
