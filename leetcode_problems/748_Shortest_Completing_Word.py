"""
 Find the minimum length word from a given dictionary words, which has all the letters from the string licensePlate. Such a word is said to complete the given string licensePlate

Here, for letters we ignore case. For example, "P" on the licensePlate still matches "p" on the word.

It is guaranteed an answer exists. If there are multiple answers, return the one that occurs first in the array.

The license plate might have the same letter occurring multiple times. For example, given a licensePlate of "PP", the word "pair" does not complete the licensePlate, but the word "supper" does.

Example 1:

Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
Output: "steps"
Explanation: The smallest length word that contains the letters "S", "P", "S", and "T".
Note that the answer is not "step", because the letter "s" must occur in the word twice.
Also note that we ignored case for the purposes of comparing whether a letter exists in the word.

Example 2:

Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
Output: "pest"
Explanation: There are 3 smallest length words that contains the letters "s".
We return the one that occurred first.

Note:

    licensePlate will be a string with length in range [1, 7].
    licensePlate will contain digits, spaces, or letters (uppercase or lowercase).
    words will have a length in the range [10, 1000].
    Every words[i] will consist of lowercase letters, and have length in range [1, 15].
"""


class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        # Solution 1: self, slow
        # import re
        # import collections

        #  matches any single character not in brackets of licensePlate and replace it with empty string
        #  as we are interested about only letters
        # s = re.sub(r'[^A-Z-a-z]+', "", licensePlate)
        # print(s)

        # c = collections.Counter(s.lower())

        # result = []
        # for each in words:
        #     w = collections.Counter(each.lower())

        #     for key in c.keys():
        #         # word can have more than required of each letter in licensePlate
        #         if not c[key] <= w[key]:
        #             break
        #     else:
        #         result.append(each)
        # # asked for minimum length
        # result = sorted(result, key=lambda x: len(x))
        # print(result)

        # return result[0]  # guranteed to have answer

        # Solution 2: sorting the given words first, fastest
        import re

        s = re.sub(r'[^A-Z-a-z]+', "", licensePlate).lower()
        print(s)

        words = sorted(words, key=lambda x: len(x))

        for w in words:
            temp = s
            for ch in w:
                temp = temp.replace(ch, '', 1)
                if len(temp) == 0:
                    return w

        # Solution 3: using built-in python fuction to check character, faster

        # l = [ch.lower() for ch in licensePlate if ch.isalpha()]
        # l = "".join(l)

        # # sort word by their length
        # words = sorted(words, key=lambda x: len(x))
        # print(words)

        # for w in words:
        #     temp = l

        #     for ch in w.lower():

        #             # replace the first occurance of character in licensePlate
        #         temp = temp.replace(ch, '', 1)
        #         #print(ch, temp)

        #         if len(temp) == 0:
        #             return w


sol = Solution()
l = "GrC8950"
w = ["measure", "other", "every", "base", "according",
     "level", "meeting", "none", "marriage", "rest"]

print(sol.shortestCompletingWord(l, w))
"""
corner case:
1. word in words dictionary can have multiple letter of each each in licensePlate
"""
