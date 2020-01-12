"""
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true

Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.

Note:

    name.length <= 1000
    typed.length <= 1000
    The characters of name and typed are lowercase letters.
"""


class Solution:
    def isLongPressedName(self, name, typed):
        # Solution 1: self, fastest, two pointer
        # O(n+m)
        # if not name or not typed:
        #         return False
        # elif len(name) > len(typed):
        #     return False

        # i = 0
        # j = 0

        # while i < len(name) and j < len(typed):
        #     #print(i, j)
        #     if name[i] != typed[j]:
        #         return False
        #     else:
        #         if i + 1 < len(name) and name[i + 1] != typed[j]:
        #             while j < len(typed) and typed[j] != name[i+1]:
        #                 j += 1
        #         else: # covers corner case #3
        #             j+=1
        #     i += 1
           
            
        # if i < len(name): # covers corner case #4
        #     return False
        # return True

        # Solution 2: same but more clean
        # if not name or not typed:
        #     return False
        # elif len(name) > len(typed):
        #     return False
        # print(len(typed))
        # i = 0
        # j = 0
        # while i <= len(name)-1:
            
        #     if name[i] == typed[j]:
        #         i += 1
        #         j += 1
        #     else:
        #         j += 1  # tackle corner case #3
        #     print(i, j)
            
        #     if j == len(typed) and i != len(name): # covers corner case #4
        #         return False

        # return True

        # Solution 3: fastest,clean and efficient

        i, n = 0, len(name)
        prev = ''
        for letter in typed:
            #print(name[i], letter)
            if i < n and letter == name[i]:
                i += 1
            elif letter != prev:
                return False
            prev = letter
        return i == n


sol = Solution()
name = "kikcxmvzi"
typed = "kiikcxxmmvvzz"
print(sol.isLongPressedName(name,typed))
"""
corner case:
1. string length less than 2
2. len(name) > len(typed)
3. name = "leelee", typed = "lleeelee"
4. name = "kikcxmvzi", typed = "kiikcxxmmvvzz"

"""
