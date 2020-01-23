"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.
Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""
# Solution 1:


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = float("Inf")
        self.queue = []

    def push(self, x: int):

        if x < self.min:
            self.min = x
        self.queue.append(x)

    def pop(self):
        x = self.queue.pop()

        self.min = float("Inf")
        for each in self.queue:
            if each < self.min:
                self.min = each
        return x

    def top(self):
        return self.queue[-1]

    def getMin(self):
        return self.min

# Solution 2:


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = []
        self.queue = []

    def push(self, x: int):

        self.queue.append(x)

        if not self.min or x < self.min[-1]:
            self.min.append(x)
        else:
            self.min.append(self.min[-1])

    def pop(self):
        self.queue.pop()
        self.min.pop()

    def top(self):
        return self.queue[-1]

    def getMin(self):
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
