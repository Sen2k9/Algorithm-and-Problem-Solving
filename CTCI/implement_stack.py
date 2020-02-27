class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyStack:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val):
        curr = self.head
        while curr:
            if not curr.next:
                node = Node(val)
                curr.next = node
                self.tail = curr.next
                break
            curr = curr.next
        if not self.head:
            node = Node(val)
            self.head = node
            self.tail = self.head

    def pop(self):
        if not self.tail:
            return "Error"

        node = self.tail
        prev = None
        curr = self.head
        while curr:
            if curr.next == self.tail:
                prev = curr
                curr.next = None
                break
            curr = curr.next
        self.tail = None
        if not prev:

            self.tail = prev
            self.head = prev
        else:
            self.tail = prev
        return node.val

    def is_empty(self):
        if not self.head and not self.tail:
            return True
        return False


stack = MyStack()
stack.add(1)
stack.add(2)
# stack.add(3)
print(stack.pop())
print(stack.head.val)
print(stack.tail.val)

print(stack.is_empty())
print(stack.pop())
print(stack.is_empty())
