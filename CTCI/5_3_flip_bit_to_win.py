"""
Flip Bit to Win:
You have an integer and you can flip exactly one bit from a 0 to a 1.
Write code to find the length of the longest sequence of 1s you could create.
Example:
Input : 1775
Output : 8
"""


class Solution:

    def __init__(self):
        pass

    def flip_bit_to_win(self, number):
        prevLength = 0
        currLength = 0
        maxLength = 1

        while number != 0:

            if (number & 1) == 1:
                currLength += 1
                maxLength = max(prevLength + currLength, maxLength)
                # O(1) operation

            else:
                if (number & 2) == 0:

                    maxLength = max(prevLength + currLength + 1, maxLength)
                    # O(1) operation
                elif (number & 1) == 0:

                    prevLength = currLength + 1
                    currLength = 0
            number = number >> 1
            # print(maxLength)
        return maxLength


if __name__ == '__main__':
    sol = Solution()
    print(sol.flip_bit_to_win(1))
"""
Complexity analysis:
Time complexity : O(b), where b is the bit number of the number which is b=logn
Space complexity : O(1), we just used couple of variables to save intermediate values
"""
