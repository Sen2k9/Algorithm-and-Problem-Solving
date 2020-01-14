"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false

Example 2:

Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode):
        # Solution 1: self
        # O(n) time and O(n) space complexity
        # stack = []

        # while not head or not head.next:
        #     return True
        # stack.append(head.val)

        # while head.next:  # O(n)
        #     node = head.next
        #     # if stack[-1] == node.val:
        #     #     stack.pop()
        #     # else:
        #     stack.append(node.val)

        #     head = node
        # i = 0
        # j = len(stack) - 1
        # while i <= j:  # O(n)
        #     if stack[i] == stack[j]:
        #         i += 1
        #         j -= 1
        #     else:
        #         return False

        # return True

        # Solution 2: slower but space efficient
        # O(n) time, O(1) space complexity

        mid = tail = head

        while tail and tail.next:
            mid = mid.next
            tail = tail.next.next

        if not mid:
            return True
        if not mid.next:
            return head.val == mid.val

        tail = mid.next.next
        mid.next.next = mid
        mid = mid.next
        mid.next.next = None

        while tail:
            new = tail.next

            tail.next = mid

            mid = tail
            tail = new

        tail = mid

        while tail and head.val == tail.val:
            head = head.next
            tail = tail.next

        return not tail


"""
corner case:
1. [1,0,1]

reference:
https://leetcode.com/problems/palindrome-linked-list/discuss/433197/Python-Time%3AO(n)-98.5-Space%3AO(1)-100.0-full-comment-comment-picture
"""
