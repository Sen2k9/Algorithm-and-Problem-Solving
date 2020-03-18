#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getStrength' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING password
#  2. INTEGER weight_a
#


def getStrength(password, weight_a):
    end_point = 25 - weight_a
    end_chr = chr(end_point + 97)
    # print(end_chr)
    ans = 0
    for c in password:
        if c <= end_chr:
            #print((ord(c) - ord("a")))
            ans = ans + (ord(c) - ord("a")) + weight_a
        else:
            ans = ans + ord(c) - ord(end_chr)-1
        print(ans)
    return ans


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    password = "aaa"

    weight_a = 0

    strength = getStrength(password, weight_a)
    print(strength)

    #fptr.write(str(strength) + '\n')

    # fptr.close()
