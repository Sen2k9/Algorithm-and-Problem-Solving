# Suppose this is foo3.py.


def functionA():
    print("a1")
    print("before import")
    from foo3 import functionB
    print("after import")
    print("a2")
    functionB()
    print("a3")


def functionB():
    print("b")


print("t1")
print("m1")
functionA()
print("m2")
print("t2")
print(__name__)
