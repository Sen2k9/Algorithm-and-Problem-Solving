class Solution:
    def isUnique(self, s):
        # Solution 1:
        # return len(list(s)) == len(set(s))

        # Solution 2:
        # O(n^2)
        # if len(s) < 2:
        #     return s
        # for i in range(len(s)):
        #     if i != len(s)-1 and s[i] in s[i + 1:]:
        #         return False
        # return True

        # Solution 3:
        # O(n)
        # alphabet = [False] * 128

        # for each in s:

        #     val = ord(each)
        #     #print(val)
        #     if alphabet[val]:
        #         return False
        #     alphabet[val] = True
        # return True

        # Solution 4: bit vector

        checker = 0

        for each in s:
            val = ord(each) - ord("a")
            # print(bin(val))
            #print(bin(1 << val))

            if (checker & (1 << val)) > 0:
                return False

            checker = checker | (1 << val)
            # print(bin(checker))
        return True

        # Solution 5: checking every other character for a character. O(n^2)
        # Solution 6: sorting all character, then checking the neighboring characters


sol = Solution()
s = "abcda"
print(sol.isUnique(s))
