"""
module to test circular import concepts
"""


import module1
import sys


def functionC():
    print("I am functionC in module 2")
    module1.fuctionA()  # calling functionA() from module 1


def functionD():
    print("I am fuctionD in module 2")


print("echo from module 2")

print("module1 imported testing in module2: %s" %
      ("module1" in sys.modules))
print("module2 imported testing in module2: %s" %
      ("module2" in sys.modules))
functionC()
functionD()

print("module2 dir ", dir())

print("returning from module 2")
