"""
Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.

Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]

Example 2:

Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]

Note:

    1 <= text.length <= 1000
    text consists of space separated words, where each word consists of lowercase English letters.
    1 <= first.length, second.length <= 10
    first and second consist of lowercase English letters.

"""


class Solution:
    def findOcurrences(self, text: str, first: str, second: str):
        # Solution 1: efficient
        result = []
        f, s = False, False

        for t in text.split():
            if f and s:
                result.append(t)
                f, s = False, False

            if t == first:
                f, s = True, False
            elif t == second:
                s = f and True
            else:
                f, s = False, False

        return result

        # Solution 2: easy to understand but kills little bit run-time for loop-up in array

        # output = []
        # text = text.split()

        # for i in range(len(text) - 2):
        #     if text[i] == first and text[i + 1] == second:
        #         output.append(text[i + 2])
        # return output


sol = Solution()
text = "ypkk lnlqhmaohv lnlqhmaohv lnlqhmaohv ypkk ypkk ypkk ypkk ypkk ypkk lnlqhmaohv lnlqhmaohv lnlqhmaohv lnlqhmaohv ypkk ypkk ypkk lnlqhmaohv lnlqhmaohv ypkk"
first = "lnlqhmaohv"
second = "ypkk"
print(sol.findOcurrences(text, first, second))
"""
corner case:
1. as each words immediately comes one after another, so after we have seen the second word, the next word will be the third
2. wrong first value
"alice is aa good girl she is a good student"
"a"
"good"

3. multiple first and second
"ypkk lnlqhmaohv lnlqhmaohv lnlqhmaohv ypkk ypkk ypkk ypkk ypkk ypkk lnlqhmaohv lnlqhmaohv lnlqhmaohv lnlqhmaohv ypkk ypkk ypkk lnlqhmaohv lnlqhmaohv ypkk"
"lnlqhmaohv"
"ypkk"

4. intermediate words between first and second
"obo jvezipre obo jnvavldde jvezipre jvezipre jnvavldde jvezipre jvezipre jvezipre y jnvavldde jnvavldde obo jnvavldde jnvavldde obo jnvavldde jnvavldde jvezipre"
"jnvavldde"
"y"

reference:
https://leetcode.com/problems/occurrences-after-bigram/discuss/341301/Python-3
"""
