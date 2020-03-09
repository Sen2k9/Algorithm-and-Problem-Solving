"""
Given a string s. You should re-order the string using the following algorithm:

    Pick the smallest character from s and append it to the result.
    Pick the smallest character from s which is greater than the last appended character to the result and append it.
    Repeat step 2 until you cannot pick more characters.
    Pick the largest character from s and append it to the result.
    Pick the largest character from s which is smaller than the last appended character to the result and append it.
    Repeat step 5 until you cannot pick more characters.
    Repeat the steps from 1 to 6 until you pick all characters from s.

In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.
Example 1:

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

Example 2:

Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.

Example 3:

Input: s = "leetcode"
Output: "cdelotee"

Example 4:

Input: s = "ggggggg"
Output: "ggggggg"

Example 5:

Input: s = "spo"
Output: "ops"

Constraints:

    1 <= s.length <= 500
    s contains only lower-case English letters.
"""


class Solution:
    def sortString(self, s: str):
        # Solution 1: brute-force
        # Time : O(nlogn)
        # Space : O(n)
        # length = len(s)
        # if length <= 1:
        #     return s

        # count_by_key = {}
        # for each in s:
        #     if each in count_by_key:
        #         count_by_key[each] += 1
        #     else:
        #         count_by_key[each] = 1
        # keys = set(count_by_key.keys())
        # ascending_keys = sorted(list(keys))
        # descending_keys = sorted(keys, reverse=True)
        # i = len(ascending_keys)-1
        # j = len(descending_keys)-1
        # result = []
        # print(length)
        # for k in range(len(s)):
        #     print(i, j)

        #     if j < 0 and i >= 0:
        #         if count_by_key[ascending_keys[i]]:
        #             result.append(ascending_keys[i])
        #             count_by_key[ascending_keys[i]] -= 1
        #         if count_by_key[ascending_keys[i]] == 0:
        #             key = ascending_keys[i]
        #             ascending_keys.remove(key)
        #             descending_keys.remove(key)

        #         i -= 1
        #         if i < 0:
        #             j = len(ascending_keys)-1
        #     elif j >= 0:
        #         if count_by_key[descending_keys[j]]:
        #             result.append(descending_keys[j])
        #             count_by_key[descending_keys[j]] -= 1
        #         if count_by_key[descending_keys[j]] == 0:
        #             key = descending_keys[j]
        #             descending_keys.remove(key)
        #             ascending_keys.remove(key)
        #         j -= 1
        #         if j < 0:
        #             i = len(ascending_keys)-1

        #     print(ascending_keys, descending_keys)
        # print(count_by_key)
        # return "".join(result)

        # Solution 2: clean and understandable
        size = len(s)
        if size == 1:  # single character string
            return s

        count_by_key = {}
        from collections import Counter
        #count_by_key = Counter(s)
        for letter in s:
            if letter in count_by_key:
                count_by_key[letter] += 1
            else:
                count_by_key[letter] = 1
        unique_characters = list(set(s))
        ascending_sort = sorted(unique_characters)
        result = []

        count = 0

        while count != size:

            for letter in ascending_sort:

                if count_by_key[letter]:
                    result.append(letter)
                    count_by_key[letter] -= 1
                    count += 1

            for letter in ascending_sort[::-1]:
                if count_by_key[letter]:
                    result.append(letter)
                    count_by_key[letter] -= 1
                    count += 1

        return "".join(result)


sol = Solution()
#s = "leetcode"
s = "defjkqvwxyzjkx"
print(sol.sortString(s))

"""
algo:
1. take count/frequency of every character : O(n), O(n)
2. sort them in ascending and descending order : O(nlogn), O(nlog)
3. iterate until length of the original string. O(n)
4. remove every string which have been used completly (means count[character] ==0) : O(n)

total runtime : O(nlogn), 
Space : O(n)
"""
