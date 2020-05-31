"""
you have two numbers represented by a linked list, where each node contains a single digit. 
The digits are stored in reverse order, such that the 1's digit is at the head of the list. 
Write a function that adds the two numbers and returns the sum as a linked list.

EXAMPLE
Input : (7 ->1 -> 6) + (5 -> 9 -> 2). That is 617 + 295
output : 2 -> 1 -> 9. That is 912

Follow up:
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
Input : (6 -> 1 -> 7) + (2 -> 9 -> 5). That is 617 + 295
output : 9 -> 1 -> 2. That is 912
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:

    def sumList(self, head1, head2):

        # Solution for the follow up

        head1 = self.reverseList(head1)  # reversing the given linkedlist
        head2 = self.reverseList(head2)  # reversing the given linkedlist

        # summation operation
        ans = Node(0)
        dummy = ans
        carry = 0

        while head1 and head2:

            total = head1.val + head2.val + carry

            val = total % 10  # for binary number total % 2
            carry = total // 10  # for binary number total // 2

            ans.next = Node(val)

            head1 = head1.next
            head2 = head2.next
            ans = ans.next

        while head1:
            total = head1.val + carry

            val = total % 10
            carry = total // 10

            if not carry:
                ans.next = head1
                break

            ans.next = Node(val)
            head1 = head1.next

        while head2:
            total = head2.val + carry
            val = total % 10
            carry = total // 10

            if not carry:
                ans.next = head2
                break

            ans.next = Node(val)
            head2 = head2.next

        if carry:
            ans.next = Node(carry)
            carry -= 1

        return self.reverseList(dummy)

    def reverseList(self, head):  # reverse a linkedlist
        prev = None

        while head:
            temp = head.next
            head.next = prev

            prev = head

            head = temp

        return prev


"""
can you solve the same problem using binary numbers?

input: (1-> 0 -> 1 -> 0) + (1 -> 1 -> 1 -> 1). That is 1010 + 1111
output:  1 -> 1 -> 0 -> 0 -> 1 . That is 11001
"""
