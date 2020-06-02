"""
Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.
"""
from collections import defaultdict


class Node:
    def __init__(self, val):
        self.val = val


class Solution:

    def loop(self, head):
        # node_dic = defaultdict(int)

        # while head:
        #     if id(head) in node_dic:
        #         return node_dic[id(head)]

        #     node_dic[id(head)] = head

        # two pointer

        slow = head
        fast = head

        while slow and fast:
            slow = slow.next
            fast = fast.next.next

        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast
