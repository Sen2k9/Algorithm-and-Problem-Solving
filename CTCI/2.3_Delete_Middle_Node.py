"""
Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
"""


def deleteMid(node):
    if not node or not node.next:
        return

    temp = node.next.data  # copy the next node data
    node.data = temp
    node.next = node.next.next  # delete the next node
