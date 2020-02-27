class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def removedups(self, head):
        # seen = set()
        # node = head
        # while node and node.next:
        #     seen.add(node.val)

        #     if node.next.val in seen:
        #         node.next = node.next.next
        #     node = node.next
        # if node and node.val in seen:
        #     node = None
        # return head

        # Solution 1: using previous node

        prev = None
        seen = set()

        curr = head
        while curr:

            if curr.val in seen:
                prev.next = curr.next

            else:
                seen.add(curr.val)
                prev = curr
            curr = curr.next
        return head

        # Solution 2: time: O(n^2), space: O(1)

        # curr = head

        # while curr:
        #     runner = curr
        #     while runner:
        #         if runner.val == curr.val:
        #             runner.next = runner.next.next

        #         runner = runner.next
        #     curr = curr.next
        # return head
