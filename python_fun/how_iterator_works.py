# import pdb


# class Test:
#     def __init__(self, limit):
#         self.limit = limit  # stop limit

#     def __iter__(self):  # this function is called when the object needs to iterate
#         self.x = 5  # built-in iterator initialize it to zero
#         return self

#     def __next__(self):  # this function receives the return value from __iter__ and executes until raise by StopIteration
#         x = self.x
#         if x >= self.limit:
#             raise StopIteration

#         self.x = x + 1
#         return x


# # pdb.set_trace()
# for i in Test(15):
#     print(i)

# list_comp = [i for i in range(10) if i % 2 == 0]

# gen_exp = (i*2 for i in range(10) if i % 2 == 0)
# print(list_comp)
# print(gen_exp)

# for each in gen_exp:
#     print(each)


# def even_integer(n):
#     for i in range(n):
#         if i % 2 == 0:
#             yield i


# integer = even_integer(10)
# print(next(integer))
# print(next(integer))
# print(next(integer))
# print(next(integer))
# print(next(integer))
# print(next(integer))

# def fibonacci_seq():

#     trail, lead = 0, 1

#     while True:
#         yield lead

#         trail, lead = lead, trail + lead


# fib = fibonacci_seq()

# for _ in range(10):
#     print(next(fib))

# from contextlib import contextmanager


# @contextmanager
# def simple_object(obj):

#     try:
#         obj.some_property += 1
#         yield

#     finally:
#         obj.some_property -= 1

def counter(string):
    count = 0
    try:
        while True:
            item = yield
            if isinstance(item, str):
                if item in string:
                    count += 1
                    print(item)

                else:
                    print("No Match")

            else:
                print("Not a string")

    except GeneratorExit:
        print(count)


c = counter("california")
next(c)
print(c.send("cali"))
print(c.send("nia"))
