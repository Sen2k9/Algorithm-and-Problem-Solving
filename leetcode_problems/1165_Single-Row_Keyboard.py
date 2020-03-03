"""
There is a special keyboard with all keys in a single row.

Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25), initially your finger is at index 0. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index i to index j is |i - j|.

You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.

Example 1:

Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
Output: 4
Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
Total time = 2 + 1 + 1 = 4. 

Example 2:

Input: keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
Output: 73

Constraints:

    keyboard.length == 26
    keyboard contains each English lowercase letter exactly once in some order.
    1 <= word.length <= 10^4
    word[i] is an English lowercase letter.

"""


class Solution:
    def calculateTime(self, keyboard: str, word: str):
        # Solution 1:
        # Time : O(n), where n is the number of words in word array
        # Space : O(26) ~ O(1)
        # dic = {}
        # for index, c in enumerate(keyboard): #O(26) ~ O(1)
        #     dic[c] = index
        # total_time = dic[word[0]]
        # for i in range(1, len(word)): #O(n)
        #     total_time += abs(dic[word[i]] - dic[word[i - 1]])
        # return total_time

        # Solution 2:
        # Time : O(n), where n is the number of words in word array
        # Space : O(26) ~ O(1)

        dic = {}

        for index, c in enumerate(keyboard):
            dic[c] = index
        total_time = 0
        curr_time = 0

        for each in word:
            total_time = total_time + abs(dic[each]-curr_time)
            curr_time = dic[each]
        return total_time


sol = Solution()
keyboard = "pqrstuvwxyzabcdefghijklmno"
word = "leetcode"
print(sol.calculateTime(keyboard, word))
