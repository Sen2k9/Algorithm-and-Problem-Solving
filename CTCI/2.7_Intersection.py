"""
Given two singly linked list, determine if the two lists intersect. Return the intersecting node. 
Note that the intersection is defined based on reference, not value. 
That is, if the kth node of the first linked list is the exact same node (by referece) as the jth node of the second linked list, then they are intersecitng.
"""
from collections import defaultdict


def intersection(head1, head2):

    # while head1:
    #     copy_head2 = head2

    #     while copy_head2:
    #         if copy_head2 == head1:
    #             return copy_head2

    #         copy_head2 = copy_head2.next

    #     head1 = head1.next

    # ref_dic = defaultdict(int)

    # while head1:

    #     ref_dic[id(head1)] = head1

    #     head1 = head1.next

    # while head2:

    #     if id(head2) in ref_dic:
    #         return ref_dic[id(head2)]

    #     head2 = head2.next

    # calculating length of two list and compare

    # get length and tail
    length1, tail1 = self.findLength(head1)
    length2, tail2 = self.findLength(head2)

    # if the tail are not equal means two list are parallel
    if tail1 != tail2:
        return None

    # truncate from the forward if the length is not equal
    if length1 == length2:
        return self.findMatch(head1, head2)

    elif length1 > length2:
        for _ in range(length1 - length2):
            head1 = head1.next

        return self.findMatch(head1, head2)

    else:
        for _ in range(length2 - length1):
            head2 = head2.next

        return self.findMatch(head1, head2)


def findMatch(self, head1, head2):

    while head1:
        if head1 == head2:
            return head1
        head1 = head1.next
        head2 = head2.next

    return None


def findLength(self, head):
    node = Node(0)
    node = head

    count = 0
    last_node = None

    while node:
        last_node = node
        count += 1

        node = node.next

    return count, last_node
