class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None


def partition(node, x):

    beforeStart = None
    beforeEnd = None
    afterStart = None
    afterEnd = None

    while node:
        nextNode = node.next
        node.next = None

        if node.val < x:
            if not beforeStart:
                beforeStart = node
                beforeEnd = beforeStart

            else:
                beforeEnd.next = node
                beforeEnd = beforeEnd.next

        else:
            if not afterStart:
                afterStart = node
                afterEnd = afterStart

            else:
                afterEnd.next = node
                afterEnd = afterEnd.next

        node = nextNode

    if not beforeStart:
        return afterStart

    if not afterStart:
        return beforeStart

    beforeEnd.next = afterStart  # merge the two linkedlist

    return beforeStart


"""
creating two separate linkedlist for small and greater/equal values in one single pass, and merge them
"""
