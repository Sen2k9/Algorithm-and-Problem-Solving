"""
Implement an algorithm to find the kth to last element of a singly linked list.
"""


def kthTolast(head, k):
    # iterative, optimal
    p1 = head
    p2 = head

    for _ in range(k):
        if p1 == None:
            return None  # out of bound

        p1 = p1.next

    while p1:
        p2 = p2.next
        p1 = p1.next

    return p2
