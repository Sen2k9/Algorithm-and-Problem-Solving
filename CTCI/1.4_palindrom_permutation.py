from collections import defaultdict


class Solution:

    def palindromPermutation(self, string):
        if len(string) < 2:
            return True

        check = self.bitvector(string)

        return check == 0 or self.checkOddOne(check)

    def bitvector(self, string):

        bit = 0

        for each in string.lower():
            val = ord(each)

            mask = 1 << val

            if bit & mask == 0:
                bit = bit | mask
            else:
                bit = bit & ~mask

        return bit

    def checkOddOne(self, bit):

        return bit & (bit-1) == 0

        # Solution 1

        # freq = defaultdict(int)

        # for each in string.lower():
        #     if each in freq:
        #         freq[each] -= 1
        #     else:
        #         freq[each] += 1

        #     if freq[each] == 0:
        #         del freq[each]
        #     # print(freq)

        # key = 0
        # for _, v in freq.items():
        #     if v > 1:
        #         return False
        #     key += 1
        #     if key > 1:
        #         return False

        # return True


sol = Solution()
print(sol.palindromPermutation(""))
print(sol.palindromPermutation("a"))
print(sol.palindromPermutation("tactcoa"))

print(sol.palindromPermutation("AmanaplanacanalPanama"))
"""
tacocat
madam, 
racecar
"A man, a plan, a canal, Panama"
"""
