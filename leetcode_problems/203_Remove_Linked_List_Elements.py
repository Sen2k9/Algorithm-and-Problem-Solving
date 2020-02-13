"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeElements(self, head, val: int):
        # Solution 1: self
        while head:
            if head.val == val:
                head = head.next
            else:
                break
        else:
            return head
        if head:
            node = head
        else:
            return head

        while node and node.next:

            if node.next.val == val:
                node.next = node.next.next

            else:
                node = node.next

            # print(node.val)
        return head

        # Solution 2: faster
        dummy = prev = ListNode("Inf")
        dummy.next = head

        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next

        return dummy.next


"""
references:
https://leetcode.com/problems/remove-linked-list-elements/discuss/473204/Python3-simple-iterative-solution
"""
