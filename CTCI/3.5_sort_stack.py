"""
Write a program to sort a stack such that the smallest items are on the top. 
You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array).
The stack supports the following operations : push, pop, peek, and isEmpty.
"""


class SortStack:

    # constructor

    def __init__(self):
        self.stack = None
        self.tempStack = []

    def sort(self, array):

        self.stack = array

        while self.stack:  # O(n)

            temp = self.stack.pop()
            count = 0

            while self.tempStack and temp < self.tempStack[-1]:
                self.stack.append(self.tempStack.pop())
                count += 1

            self.tempStack.append(temp)

            for _ in range(count):  # O(n), this one works as nested loop
                self.tempStack.append(self.stack.pop())

        while self.tempStack:
            self.stack.append(self.tempStack.pop())

        return self.stack


sol = SortStack()
print(sol.sort([1, 2, 3, 4, 5]))


"""
time complexity : O(n^2), selection sort
space complexity : O(1), because we did not use any extra memory except some variables
"""
