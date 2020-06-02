"""
Implement a function to check if a linked list is a palindrome
"""


class DoublyList:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class SinglyList:
    def __init__(self, val):
        self.val = val
        self.next = next


class Solution:

    def palindrome(self, head: SinglyList):
        # For doubly linkedlist
        # count = 0

        # start = head
        # end = head

        # while end:
        #     count += 1
        #     end = end.next

        # for _ in range(count//2):
        #     if start.val != end.val:
        #         return False

        #     start = start.next
        #     end = end.prev

        # For singly linkedlist reverse the list

        #     copy = head

        #     copy, count = self.reverseList(copy, prev=None)

        #     while count > count//2:
        #         if head.val != copy.val:
        #             return False
        #         head = head.next
        #         copy = copy.next
        #         count -= 1

        #     return True

        # def reverseList(self, head, prev):
        #     count = 0

        #     while head:

        #         temp = head.next

        #         head.next = prev

        #         prev = head

        #         head = temp
        #         count += 1

        #     return prev, count

        # For singly linkedlist iterative approach : stack

        stack = []

        slow = head
        fast = head

        while fast and fast.next:
            stack.append(slow.val)

            fast = fast.next.next
            slow = slow.next

        if not fast:
            stack.pop()

        while slow.next:
            if slow.next.val != stack[-1]:
                return False

            slow = slow.next
            stack.pop()

        if not stack:
            return True


"""
O(n)
"""
