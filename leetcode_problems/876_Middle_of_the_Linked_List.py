"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.

Note:

    The number of nodes in the given list will be between 1 and 100.

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def middleNode(self, head):
        # Solution 1: self
        # O(n)
        # dic = {}
        # count = 1
        # dic[count] = head

        # while head.next:
        #     head = head.next
        #     count += 1
        #     dic[count] = head

        # mid = count // 2
        # return dic[mid + 1]

        # Solution 2: faster
        object1 = head
        object2 = head
        while object1 and object1.next:
            object1 = object1.next.next
            object2 = object2.next
        return object2


sol = Solution()
"""
If object 1(hare) is moving at speed of 2x and object2(tortoise) at speed of x than object2 will be on halfway when the object1 complete the distance.
reference:
https://leetcode.com/problems/middle-of-the-linked-list/discuss/396938/faster-than-98.10-of-Python3-online-submissions-for-Middle-of-the-Linked-List.
"""
