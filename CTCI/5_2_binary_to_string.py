"""
Binary to String: Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double,
print the binary representation. If the number cannot be represented accurately in binary with at most 32 characters,
print "ERROR".
"""

class Solution:

    def __init__(self):
        pass 

    def binaryTostring(self,num):

        if num >= 1 and num < 0:
            return "ERROR"

        array = ["0."]

        while num > 0:

            if len(array) > 32:
                return "ERROR"

            r = num * 2

            if r >= 1:
                array.append("1")
                num = r - 1
            else:
                array.append("0")
                num = r


            #print(array, num)

        return "".join(array)

if __name__ == '__main__':
    sol = Solution()
    print(sol.binaryTostring(0.625))

