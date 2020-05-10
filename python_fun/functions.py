
import math
from math import factorial as fact

print(fact(5))
hello = math.factorial(6)
print(hello)
print("hello")


def f(a, b, c=10, d=None):
    pass


def g(a=10, b=20, c=30):
    pass


def h(a, *b, c=10):
    pass


h(1, 2, 3, 4, 5)
h(1, 2, 3, 4, c=5)
h(a=1, 2, 3, 4, c=5)
h(1, 2, 3, 4, c=5, a=1)


f(1, 2, 3, 4)
f(1, 2, 3)
f(1, 2)
f(1)
f(1, 2, b=3)
f(d=1, b=2)
f(b=1, a=2)
f(a=1, d=2, b=3)
f(2, 3, c=1)
g()
g(b=1)
g(a=1, 2, c=3)
