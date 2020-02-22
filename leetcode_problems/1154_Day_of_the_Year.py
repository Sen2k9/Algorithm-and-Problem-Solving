"""
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

 

Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.

Example 2:

Input: date = "2019-02-10"
Output: 41

Example 3:

Input: date = "2003-03-01"
Output: 60

Example 4:

Input: date = "2004-03-01"
Output: 61

Constraints:

    date.length == 10
    date[4] == date[7] == '-', and all other date[i]'s are digits
    date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
"""


class Solution:
    def dayOfYear(self, date: str):
        # Solution 1:
        year, month, day = date.split("-")
        #print(year, month, day)
        dic = {1: 0, 2: 31, 3: 28, 4: 31, 5: 30, 6: 31,
               7: 30, 8: 31, 9: 31, 10: 30, 11: 31, 12: 30, 13: 31}

        res = 0
        leap_year = False
        if int(year) % 4 == 0 and int(month) >= 2:  # find the leap year
            if not int(year) % 100 == 0 or int(year) % 400 == 0:
                leap_year = True

        m = int(month)
        if m > 12:
            m = 12
        for i in range(1, m + 1):  # counting all the day
            res += dic[i]

        # checking whether the given day is in the range for the month, e.g., for January the day <=31
        if int(day) <= dic[m + 1]:
            if leap_year:

                # even if the year is leap year if the date is "2012-02-04" then we should not add +1
                if int(month) > 2:
                    return res + int(day) + 1
                else:  # only if leap year and month >2
                    return res+int(day)
            else:
                return res+int(day)
        else:  # if input is "2012-02-29" then the if clause will fail, which will catch by this else
            if leap_year:

                return res + dic[m + 1] + 1
            else:
                return res + dic[m + 1]

        # Solution 2: simple and clean
        y, m, d = map(int, date.split('-'))
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (y % 400) == 0 or ((y % 4 == 0) and (y % 100 != 0)):
            days[1] = 29
        return d + sum(days[: m - 1])
        # reference: https://leetcode.com/problems/day-of-the-year/discuss/449866/Python-3-Four-liner-Simple-Solution


sol = Solution()
date = "2012-02-04"


print(sol.dayOfYear(date))
"""
Algorithm to find a leap year:
if (year is not divisible by 4) then (it is a common year)
else if (year is not divisible by 100) then (it is a leap year)
else if (year is not divisible by 400) then (it is a common year)
else (it is a leap year) 

corner case:
1. leap year
2. day more than 31
"""
