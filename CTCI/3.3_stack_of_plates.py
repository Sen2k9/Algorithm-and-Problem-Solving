

class StackOfPlates:

    # constructor
    def __init__(self, capacity=0):

        self.capacity = capacity

        self.stack = []

    def push(self, value):
        if not self.stack:

            self.firstTimeCreated(value)

        elif len(self.stack[-1]) == self.capacity:

            self.firstTimeCreated(value)

        else:
            self.stack[-1].append(value)

    def pop(self, index=None):  # python does not support method overloading but you can do it in one method using default parameters

        if index != None:
            # print(self.stack[index])
            return self.stack[index].pop()

        if not self.stack:
            return

        elif not self.stack[-1]:
            self.stack.pop()
            return self.stack[-1].pop()

        else:
            return self.stack[-1].pop()

    def firstTimeCreated(self, value):
        substack = []
        substack.append(value)
        self.stack.append(substack)


stack = StackOfPlates(2)

print(stack.push(1))
print(stack.push(2))

print(stack.push(3))

print(stack.push(4))
print(stack.push(5))

print(stack.push(6))
print(stack.stack)
print(stack.push(7))
print(stack.stack)

print(stack.pop())  # 7
print(stack.stack)

print(stack.pop())  # 6
print(stack.stack)

print(stack.pop())  # 5
print(stack.stack)

print(stack.pop())  # 4
print(stack.stack)

print(stack.pop(0))  # 2
print(stack.stack)
