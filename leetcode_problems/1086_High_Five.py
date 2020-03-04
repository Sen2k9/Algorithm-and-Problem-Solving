"""
Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.

Note:

    1 <= items.length <= 1000
    items[i].length == 2
    The IDs of the students is between 1 to 1000
    The score of the students is between 1 to 100
    For each student, there are at least 5 scores
"""


class Solution:
    def highFive(self, items):
        # Solution 1: fastest
        # time : O(nlogn)
        # space : O(n)
        # from collections import defaultdict
        # dictionary = defaultdict(list)
        # #dictionary = {[]}

        # for each in items:
        #     dictionary[each[0]].append(each[1])

        dictionary = dict()

        for each in items:
            dictionary.setdefault(each[0], []).append(each[1])

        result = []

        for key, val in dictionary.items():
            val = sorted(val, reverse=True)[:5]  # O(nlogn)
            val = sum(val)//5
            result.append([key, val])

        result = sorted(result, key=lambda x: x[0])
        return result


sol = Solution()
items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77],
         [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
print(sol.highFive(items))

"""
corner case:
1. can be only one studen with all values
"""
