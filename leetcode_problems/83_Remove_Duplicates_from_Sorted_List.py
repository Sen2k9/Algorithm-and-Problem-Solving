"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2

Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode):
        # Solution 1: self
        # Runtime : O(n)
        # Memory : O(n)
        result = curr = ListNode(0)
        dic = {}

        while head:

            if head.val in dic:
                head = head.next

            else:
                dic[head.val] = 1
                curr.next = ListNode(head.val)
                curr = curr.next
                head = head.next
            # print(dic)
        return result.next

        # Solution 2: using set, faster
        # Runtime : O(n)
        # Memory : O(n)
        result = curr = ListNode(0)
        dic = set()

        while head:

            if head.val in dic:
                head = head.next

            else:
                dic.add(head.val)
                curr.next = ListNode(head.val)
                curr = curr.next
                head = head.next
            # print(dic)
        return result.next
