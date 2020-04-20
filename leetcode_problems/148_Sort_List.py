"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4

Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5


"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def sortList(self, head: ListNode):
        if not head:
            return None
        if not head.next:
            return head

        prev = None

        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        left_merge = self.sortList(head)

        right_merge = self.sortList(slow)

        root = ListNode(None)
        new_head = root

        while left_merge and right_merge:

            if left_merge.val <= right_merge.val:
                new_head.next = left_merge
                left_merge = left_merge.next
            else:
                new_head.next = right_merge
                right_merge = right_merge.next
            # if not temp:
            #     temp = new_head

            new_head = new_head.next

        if left_merge:
            new_head.next = left_merge
            # left_merge = left_merge.next
            # new_head = new_head.next

        if right_merge:
            new_head.next = right_merge
            # right_merge = right_merge.next
            # new_head = new_head.next

        return root.next
