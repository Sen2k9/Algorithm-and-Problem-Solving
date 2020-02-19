import psutil
import timeit
import subprocess
import os
from sys import argv

# .....
# method code goes here


def method6(loop_count):
    return ''.join([str(num) for num in range(loop_count)])


# .....


# def process_num(process):
#     return commands.getoutput('pidof %s |wc -w' % process)
def ps_stat():
    #global process_size
    ps = psutil.Process(os.getpid())
    # print(ps.memory_full_info().uss)  # in bytes
    process_size = ps.memory_full_info().uss
    return process_size


# print(process.memory_percent())


def main(loop_count):
    #global process_size
    start = timeit.timeit()
    num = method6(loop_count)
    end = timeit.timeit()
    #print("method", num)
    print("time", float((end-start) / 1000000))
    print("output size ", len(num) / 1024, "kb")
    print("process size", ps_stat()/1024, "kb")
    # print()


loop_count = 500000
# pid = os.getpid()
# print(pid)
main(loop_count)

"""
references:
https://waymoot.org/home/python_string/
"""
