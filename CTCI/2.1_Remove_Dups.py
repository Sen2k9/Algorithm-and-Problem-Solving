class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def removedups(self, head):
        # Solution 1 : using set

        # prev = None
        # curr = head
        # unique = set()

        # while curr != None:

        #     if curr.val in unique:
        #         prev.next = curr.next

        #     else:
        #         unique.add(curr.val)
        #         prev = curr

        #     curr = curr.next

        # return head

        # Solution 2: O(1) space, O(n^2) runtime

        slow = head

        while slow != None:
            fast = slow
            while fast.next != None:
                if fast.next.val == slow.val:
                    fast.next = fast.next.next
                fast = fast.next

            slow = slow.next

        return head
