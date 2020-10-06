"""
Design and implement an iterator to flatten a 2d vector. It should support the following operations: next and hasNext.

Example:

Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

iterator.next(); // return 1
iterator.next(); // return 2
iterator.next(); // return 3
iterator.hasNext(); // return true
iterator.hasNext(); // return true
iterator.next(); // return 4
iterator.hasNext(); // return false
 
Notes:

Please remember to RESET your class variables declared in Vector2D, as static/class variables are persisted across multiple test cases. Please see here for more details.
You may assume that next() call will always be valid, that is, there will be at least a next element in the 2d vector when next() is called.
 

Follow up:

As an added challenge, try to code it using only iterators in C++ or iterators in Java.
"""

class Vector2D:


    def __init__(self, v):
        self.v = v  # pointing a reference of the original vector
        # initializing rows and column
        self.rows = 0
        self.col = -1
        

    def next(self) -> int:

        if self.hasNext():
            self.col += 1
            temp_row = self.rows
            temp_col = self.col
            # check whether element is exhausting for the existing row
            # if so, start fresh for column and increment 1 for rows
            if self.col == len(self.v[self.rows]) - 1:
                self.rows += 1
                self.col = -1

            return self.v[temp_row][temp_col]


        

    def hasNext(self) -> bool:
        # check rows as long as it's number does not exhaust to the length of the vector
        if self.rows < len(self.v):
            # iterate as long as we find row with non-zero elements
            for row in range(self.rows, len(self.v)):  
                if self.v[row]:
                    self.rows = row  # save that row value for further processing
                    return True
        return False

        


# Your Vector2D object will be instantiated and called as such:

#v = [[1,2],[3],[4,5,6]]

v = [[], [3]]

#v = [[]]
iterator = Vector2D(v)
# print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())
# print(iterator.next())
# print(iterator.hasNext())
# print(iterator.next())
# print(iterator.hasNext())

# print(iterator.next())
# print(iterator.hasNext())

# print(iterator.next())
# print(iterator.hasNext())