import pdb


class Test:
    def __init__(self, limit):
        self.limit = limit  # stop limit

    def __iter__(self):  # this function is called when the object needs to iterate
        self.x = 5  # built-in iterator initialize it to zero
        return self

    def __next__(self):  # this function receives the return value from __iter__ and executes until raise by StopIteration
        x = self.x
        if x >= self.limit:
            raise StopIteration

        self.x = x + 1
        return x


# pdb.set_trace()
for i in Test(15):
    print(i)
