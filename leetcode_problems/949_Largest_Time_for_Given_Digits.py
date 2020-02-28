"""
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

Example 1:

Input: [1,2,3,4]
Output: "23:41"

Example 2:

Input: [5,5,5,5]
Output: ""

Note:

    A.length == 4
    0 <= A[i] <= 9
"""


# def permutation(data):
#     l = []
#     if len(data) == 0:
#         return
#     if len(data) == 1:
#         return [data]

#     for i in range(len(data)):
#         m = data[i]
#         remaining = data[:i] + data[i + 1:]

#         for j in permutation(remaining):
#             l.append([m] + j)

#     return l


class Solution:
    def largestTimeFromDigits(self, A):
        def permutation(data):
            l = []
            if len(data) == 0:
                return
            if len(data) == 1:
                return [data]

            for i in range(len(data)):
                m = data[i]
                remaining = data[:i] + data[i + 1:]

                for j in permutation(remaining):
                    l.append([m] + j)

            return l

        if len(set(A)) == 1:
            if A[0] > 2:
                return ""

        def to_date(max_hour, max_mins):
            return "{:02d}:{:02d}".format(max_hour, max_mins)
        max_hour = -1
        max_mins = -1
        for p in permutation(A):
            # print(p)
            hrs = int(str(p[0]) + str(p[1]))
            mins = int(str(p[2]) + str(p[3]))

            if 0 <= hrs <= 23 and 0 <= mins <= 59:
                if hrs > max_hour or (hrs == max_hour and mins > max_mins):
                    max_hour = hrs
                    max_mins = mins

        if max_hour == -1 or max_mins == -1:
            return ""
        return to_date(max_hour, max_mins)


sol = Solution()
A = [1, 9, 6, 0]


print(sol.largestTimeFromDigits(A))


# Driver program to test above function
data = [1, 2, 3, 4]
# for p in permutation(data):
#     print(p)

"""
reference:
https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/
"""
