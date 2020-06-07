"""
Implement a MyQueue class which implements a queue using two stacks.
"""


class MyQueue:

    # constructor
    def __init__(self):
        self.stackNew = []
        self.stackOld = []

    def push(self, value):  # always push into new stack
        self.stackNew.append(value)

    def pop(self):
        self.shiftStack()
        if not self.stackOld:  # sanity check for empty stack
            return
        return self.stackOld.pop()

    def peek(self):
        self.shiftStack()

        if not self.stackOld:  # sanity check for empty stack
            return
        return self.stackOld[-1]

    def shiftStack(self):
        if not self.stackOld:
            while self.stackNew:
                self.stackOld.append(self.stackNew.pop())


sol = MyQueue()

print(sol.push(1))
print(sol.push(2))
print(sol.push(3))
print(sol.peek())
print(sol.pop())
print(sol.push(8))
print(sol.push(10))

print(sol.peek())
print(sol.pop())

print(sol.peek())
print(sol.pop())

print(sol.peek())
print(sol.pop())
