"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Follow up:

Can you solve it using O(1) (i.e. constant) memory?

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head, pos):
        # Solution 1: self
        # if not head:
        #     return False
        # hasSeen = []
        # while head:
        #     hasSeen.append(head)
        #     head = head.next
        #     if head in hasSeen:
        #         return True
        # return False

        # Solution 2: faster, O(1) space complexity
        # while head:
        #     if head.val == "x":
        #         return True
        #     head.val = "x"
        #     head = head.next
        # return False

        # Solution 3: two-pointer solution, fastest

        if not head or not head.next:
            return False

        p1 = p2 = head
        
        while head and head.next and head.next.next:
            p1 = head.next
            p2 = head.next.next
            if p1 == p2:
                return True

        return False







sol = Solution()
head=[3, 2, 0, -4]
pos=1
print(sol.hasCycle(head,pos))
"""
The idea of two pointer is:
if one pointer increment double than other pointer, then after some time the fastest pointer will catch the slower pointer.
If that happens then their is a cycle.
If their is not cycle then one of the pointer will have None as their next node

https://leetcode.com/problems/linked-list-cycle/discuss/372473/Python-93-Faster-Simple-Solution
"""
