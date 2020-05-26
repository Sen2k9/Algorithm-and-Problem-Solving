
class Solution:

    def compressed(self, string):
        # if len(string) < 3:
        #     return string

        # freq = {}

        # for each in string:
        #     if each not in freq:
        #         freq[each] = 1

        #     else:

        #         freq[each] += 1

        # if len(string) == len(freq):  # all unique
        #     return string

        # arr = []

        # count = 0

        # for i in range(0, len(string)):
        #     count += 1

        #     if i + 1 == len(string) or string[i + 1] != string[i]:
        #         arr.append(string[i])
        #         arr.append(str(count))
        #         count = 0

        # if len(arr) < len(string):

        #     return "".join(arr)

        # else:
        #     return string

        # Solution : optimized

        # any string length less than 3 can not be compressed. for example, "","a","aa","ab"
        if len(string) < 3:
            return string

        finalLength = self.compressedLength(string)

        # if a very large unique string comes, we can save the memory
        if finalLength > len(string):
            return string

        # now without having no other options to optimize we have to sacrifice the memory for the new compressed string

        # but here we can save the run-time by pre-defining array length so that in the backend we do not use dynamic array which uses amortize O(1) for insertion

        # save our run-time from amortize O(1) to exact O(1)
        arr = [0] * finalLength
        count = 0
        index = 0

        for i in range(len(string)):
            count += 1

            if i + 1 == len(string) or string[i + 1] != string[i]:
                arr[index] = string[i]
                arr[index+1] = str(count)

                count = 0
                index += 2
        # print(arr)

        return "".join(arr)

    def compressedLength(self, string):
        compressedLen = 0
        count = 0

        for i in range(len(string)):
            count += 1

            if i + 1 == len(string) or string[i + 1] != string[i]:

                compressedLen = compressedLen + 1 + len(str(count))

                count = 0

        return compressedLen


"""
time complexity: O(n)
space complexity : O(n)

key-points : never use string concatenation, string concatenation creates O(n^2) complexity
"""
sol = Solution()
print(sol.compressed(""))
print(sol.compressed("a"))
print(sol.compressed("aa"))
print(sol.compressed("abc"))
print(sol.compressed("aaabbcc"))
print(sol.compressed("aaabbccaa"))
