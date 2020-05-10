# Suppose this is foo.py.

import foo
import foo2
import math
import foo3
print("starting foo1.py")
print("before import foo2.py")
print("before functionA in foo1.py")


def functionA():
    print("Function A in foo1.py")


print("before functionB in foo1.py")


def functionB():
    print("Function B foo1.py {}".format(math.sqrt(100)))


print("before __name__ guard in foo1.py")
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard in foo1.py")
print(__name__)
