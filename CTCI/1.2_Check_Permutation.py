"""
Given two string, write a method to decide if one is a permutation of the other.
"""


def checkPermutation(str1, str2):

    if len(str1) != len(str2):
        return False

    check = 0

    for c in str1:
        val = ord(c)

        check = check ^ val

    for c in str2:
        val = ord(c)
        check = check ^ val

    return check == 0


print(checkPermutation("abac", "adbc"))
