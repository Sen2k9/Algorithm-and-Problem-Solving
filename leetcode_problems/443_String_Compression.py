"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

Follow up:
Could you solve it using only O(1) extra space?

Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".

Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.

Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.

Note:

    All characters have an ASCII value in [35, 126].
    1 <= len(chars) <= 1000.
"""


class Solution:
    def compress(self, chars):
        # Solution 1: self, slow
        # if len(chars) < 2:
        #     return len(chars)
        # i = 0
        # chars.append("Inf")
        # j = len(chars)-1
        # seen = ""
        # l = []

        # while i < j:

        #     seen = chars[i]
        #     l.append(seen)
        #     for k in range(len(chars) - i):
        #         # if chars[k + i] == "Inf":
        #         #     i = i+k
        #         #     break
        #         if chars[k + i] != seen:

        #             i = i + k
        #             if k > 1:
        #                 l = l + list(str(k))

        #             break
        #     print(l)

        # chars[:] = l[:]
        # return len(chars)

        # Solution 2: fastest, in-place, coming from tail reduces the computational cost

        count = 1
        for i in range(len(chars) - 1, -1, -1):
            if i > 0 and chars[i] == chars[i - 1]:
                count += 1
                chars.pop(i)

            else:
                if count > 1:
                    for each in str(count)[::-1]:
                        chars.insert(i + 1, each)
                    count = 1

        return len(chars)


sol = Solution()
chars = ["a", "a", "a", "b", "b", "a", "a"]

print(sol.compress(chars))
"""
Every element of the array should be a character (not int) of length 1.
compress it in place
["a","a","a","b","b","a","a"]

"""
