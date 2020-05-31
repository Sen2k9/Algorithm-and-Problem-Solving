class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverseList(self, head):
        prev = None

        while head:
            temp = head.next

            head.next = prev

            prev = head

            head = temp

        return prev


""""
6 -> 1 -> 7 ->None

7 -> 1 -> 6 -> None
""""
