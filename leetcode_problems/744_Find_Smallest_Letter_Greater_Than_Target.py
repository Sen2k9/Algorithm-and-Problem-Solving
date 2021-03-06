"""
 Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:

Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"

Note:

    letters has a length in range [2, 10000].
    letters consists of lowercase letters, and contains at least 2 unique letters.
    target is a lowercase letter.
"""


class Solution:
    def nextGreatestLetter(self, letters, target):
        # Solution 1: self
        # if ord(target) >= ord(letters[-1]):
        #     return letters[0]
        # #binary search
        # i = 0
        # j = len(letters)
        # while i < j:
        #     mid = (i + j) // 2
            
        #     if ord(letters[mid]) > ord(target):
        #         j = mid
        #     elif ord(letters[mid]) <= ord(target):
        #         i = mid+1
        
        # return letters[j]

        # Solution 2: using set

        letters = list(set(letters))
        letters.sort()
        for each in letters:
            if ord(each) > ord(target):
                return each
        return letters[0]


            
        

            

        

sol = Solution()
target = "j"
letters = ["c", "f", "j"]
print(sol.nextGreatestLetter(letters, target))
