"""
module to test circular import concepts
"""
import sys
import module2


def fuctionA():
    print("I am fuctionA in module 1")

    # module2.functionC()  # calling functionC() from module2


def fuctionB():
    print("I am fuctionB in module 1")


print("echo from module 1")

print("module1 imported testing in module1: %s" %
      ("module1" in sys.modules))

print("module2 dir", dir(module2))

print("module2 imported testing in module1: %s" %
      ("module2" in sys.modules))
fuctionA()
fuctionB()

print("module1 dir ", dir())
print("returning from module 1")


"""
key points:
1. import works line by line
2. Once a module is imported in sys.modules, it does not execute the import line again if found later. For exmaple the first "import sys" will be executed
import sys
import sys

3. Once module is imported it's name save to '__name__' variable, 
after python gets the chance to interpret all of the imported modules variable and function namespace, then only other module can call imported modules variable and functions

4. If in the circular import execution path does not encounter any variable or functions not interpreted, then no error comes out.
"""
