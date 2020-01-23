"""
Implement the following operations of a stack using queues.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    empty() -- Return whether the stack is empty.

Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false

Notes:

    You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
    Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
    You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""


from collections import deque

# Solution 1: brute-force


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int):
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        """
        temp = []
        for i in range(len(self.queue)-1, -1, -1):
            temp.append(self.queue[i])
        x = temp[0]
        self.queue = self.queue[:-1]
        return x

    def top(self):
        """
        Get the top element.
        """
        temp = []
        for i in range(len(self.queue)-1, -1, -1):
            temp.append(self.queue[i])
        x = temp[0]
        return x

    def empty(self):
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0


# Solution 2: faster


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.queue = deque()

    def push(self, x: int):
        """
        Push element x onto stack.
        """
        temp = deque([x])
        self.queue = temp + self.queue

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()

    def top(self):
        """
        Get the top element.
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0

# Solution 3: fastest


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.queue = []

    def push(self, x: int):
        """
        Push element x onto stack.
        """
        temp = [x]
        self.queue = temp + self.queue

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        """
        x = self.queue[0]
        self.queue[:] = self.queue[1:]
        return x

    def top(self):
        """
        Get the top element.
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
stack = MyStack()

stack.push(1)
stack.push(2)
print(stack.top())

print(stack.pop())

print(stack.empty())

"""
reference:
https://leetcode.com/problems/implement-stack-using-queues/discuss/381976/Python-solutions
"""
