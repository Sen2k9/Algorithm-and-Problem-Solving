"""
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

    Each word after the identifier will consist only of lowercase letters, or;
    Each word after the identifier will consist only of digits.

We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

Constraints:

    0 <= logs.length <= 100
    3 <= logs[i].length <= 100
    logs[i] is guaranteed to have an identifier, and a word after the identifier.

"""


class Solution:
    def reorderLogFiles(self, logs):
        # Solution 1: self
        # if not logs:
        #     return logs
        # letter_logs = []
        # digit_logs = []
        # for each in logs:
        #     s = each.split()
        #     if not s[1].isdigit():
        #         letter_logs.append(s)
        #     else:
        #         digit_logs.append(s)

        # digit_logs = [" ".join(each) for each in digit_logs]
        # sort_letter = sorted(letter_logs, key=lambda x: x[1:])
        # for i in range(len(sort_letter) - 1):
        #     if len(sort_letter) == 1:
        #         break
        #     if sort_letter[i][1:] == sort_letter[i + 1][1:]:
        #         if sort_letter[i][:1] > sort_letter[i + 1][:1]:
        #             temp = sort_letter[i]
        #             sort_letter[i] = sort_letter[i + 1]
        #             sort_letter[i + 1] = temp

        # letter_logs = [" ".join(each) for each in sort_letter]

        # return letter_logs + digit_logs

        # Solution 2: faster

        if not logs:
            return logs
        letter_logs = []
        digit_logs = []
        for each in logs:
            if each.split()[1].isdigit():
                digit_logs.append(each)
            else:
                letter_logs.append(each)

        letter_logs = sorted(letter_logs, key=lambda x: (
            x.split(" ", 1)[1], x.split(" ", 1)[0]))

        # reference: https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes

        return letter_logs + digit_logs

        # Solution 3:
        if not logs:
            return logs
        letter_logs = []
        digit_logs = []
        for each in logs:
            if each.split()[1].isnumeric():
                digit_logs.append(each)
            else:
                letter_logs.append(each.split())

        letter_logs = sorted(letter_logs, key=lambda x: x[1:]+[x[0]])

        # reference: https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
        # https://leetcode.com/problems/reorder-data-in-log-files/discuss/382667/Solution-in-Python-3-(beats-~100)-(five-lines)

        return [" ".join(each) for each in letter_logs] + digit_logs


sol = Solution()
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]
print(sol.reorderLogFiles(logs))

"""
corner case:
1. no logs
2. lexicographic ties in letter_logs

reference:
https://leetcode.com/problems/reorder-data-in-log-files/discuss/480018/Runtime%3A-99.58-Memory%3A-100
https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
"""
