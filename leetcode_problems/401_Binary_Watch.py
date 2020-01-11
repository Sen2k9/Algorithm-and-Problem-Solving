"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

Note:

    The order of output does not matter.
    The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
    The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

"""


class Solution:
    def readBinaryWatch(self, num: int):
        # result = []
        # if num > 10 or num < 1:
        #     return result

        # for i in range(12):
        #     for j in range(60):
        #         if bin(i).count("1") + bin(j).count("1") == num:
        #             h = str(i)
        #             if j < 10:
        #                 m = "0" + str(j)
        #             else:
        #                 m = str(j)
        #             result.append(h + ":" + m)
        # return result

        # Solution 2: backtracking
        import itertools


        def dfs(num, hours, result):
            if hours > num:
                return

            for hour in itertools.combinations([1, 2, 4, 8], hours):
                h = sum(hour)
                if h >= 12:
                    continue

                for minute in itertools.combinations([1, 2, 4, 8, 16, 32], num - hours):
                    m = sum(minute)
                    if m >= 60:
                        continue

                    result.append("%d:%02d" % (h, m))
                    
            dfs(num, hours + 1, result)
            
        result = []
        dfs(num, 0, result)
        return result

        


sol = Solution()
num = 3
print(sol.readBinaryWatch(num))
