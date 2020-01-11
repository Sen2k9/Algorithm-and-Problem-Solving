"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode):
        # Solution 1: self, iterative

        # if not head or not head.next:
        #     return head
        # queue = []
        # while head:
        #     queue.append(head)
        #     head = head.next
        # queue = queue[::-1]

        # for i in range(len(queue)-1):
        #     node1 = queue[i]
        #     node2 = queue[i+1]
        #     node1.next = node2
        #     node2.next = None

        # return queue[0]

        # Solution 2: self, recursive

        def reverse(node, head):
            if not node:
                return None, head
            prev_node, head = reverse(node.next, head)
            node.next = None
            if not prev_node:
                head = node
            else:
                prev_node.next = node
            return node, head

        _, head = reverse(head, head)
        return head

        # Solution 3:
        # prev_node = None
        # next_node = head

        # while next_node:
        #     curr_node = next_node
        #     next_node = curr_node.next
        #     curr_node.next = prev_node
        #     prev_node = curr_node

        # return prev_node
