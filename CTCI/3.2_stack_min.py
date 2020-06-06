"""
How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element?
Push, pop and min should all operate in O(1) time.
"""


class StackMin:
    # constructor

    def __init__(self):
        self.minValue = []
        self.stack = []
        self.index = -1

    def push(self, value):
        """
        rtype : None
        """
        if not self.minValue:
            self.minValue.append((value, self.index))

        elif self.minValue[-1][0] > value:
            self.minValue.append((value, self.index))

        self.stack.append(value)
        self.index += 1

    def pop(self):
        """
        rtype : object
        """
        #print(self.stack, self.index)
        if self.index < 0:
            return
        self.stack.pop()
        self.index -= 1
        if self.index < self.minValue[-1][1]:
            self.minValue.pop()

    def min(self):
        """
        rtype : object
        """
        if not self.minValue:
            return None

        return self.minValue[-1][0]


stack = StackMin()

assert stack.push(100) == None, "has an error"
print(stack.push(2))
print(stack.push(-1))
print(stack.push(4))
print(stack.push(5))

print(stack.pop())
print(stack.min())

print(stack.pop())
print(stack.min())

print(stack.pop())
print(stack.min())

print(stack.pop())
print(stack.min())

print(stack.pop())
print(stack.min())

print(stack.pop())
print(stack.min())
