"""
In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.

 

Note:

    1 <= time.length <= 60000
    1 <= time[i] <= 500

"""


class Solution:
    def numPairsDivisibleBy60(self, time):
        # # brute-force approach
        # pairs = 0
        # for i in range(len(time)):
        #     for j in range(i + 1, len(time)):
        #         if (time[i] + time[j]) % 60 == 0:
        #             pairs += 1
        # return pairs

        # # Solution 1:using modulo with negative number in python
        # ans = 0
        # d = dict()
        # for t in time:
        #     ans = ans + d.get((-t) % 60, 0)
        #     d[t % 60] = d.get(t % 60, 0) + 1
        #     print(d)
        # return ans
        # solution 2: Using dictionary with nC2
        from collections import Counter
        time = [item % 60 for item in time]
        # print(time)
        d = Counter(time)
        # print(d)
        pair = 0
        for each in d:
            if each == 0 or each == 30:
                if d[each] > 1:
                    # combination rule nC2
                    pair = pair + (d[each] * (d[each] - 1))
            elif (60 - each) in d:
                pair = pair + (d[each] * d[60 - each])

        return pair//2


sol = Solution()
time = [30, 20, 150, 100, 40]
print(sol.numPairsDivisibleBy60(time))

"""
https://stackoverflow.com/questions/3883004/the-modulo-operation-on-negative-numbers-in-python
"""
