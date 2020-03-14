"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

    All inputs will be in lowercase.
    The order of your output does not matter.

"""


class Solution:
    def groupAnagrams(self, strs):
        # Solution 1: using dictionary
        # dictionary = {}
        # index = 0
        # temp = []
        # for each in strs:
        #     # O(nm)
        #     s = "".join(sorted(each))
        #     temp.append(s)
        #     if s in dictionary:
        #         continue
        #     else:
        #         dictionary[s] = index
        #         index += 1
        # # print(dictionary)
        # ans = [[] for _ in range(len(dictionary.keys()))]
        # # print(ans)
        # for i in range(len(temp)):
        #     s = temp[i]
        #     # print(ans[dictionary[s]])
        #     ans[dictionary[s]].append(strs[i])

        # return ans

        # Solution 2: faster
        # time : O(nmlogm)
        # space : O(nm)
        # dictionary = {}
        # for word in strs:
        #     sorted_word = "".join(sorted(word))
        #     if sorted_word in dictionary:
        #         dictionary[sorted_word].append(word)
        #     else:
        #         dictionary[sorted_word] = [word]
        # return list(dictionary.values())

        # Solution 3 : fastest, categorize by count
        # time : O(nm)
        # space : O(nm)

        dictionary = {}
        for each in strs:
            count = [0] * 26
            for s in each:
                count[ord(s) - ord("a")] += 1
            count = tuple(count)
            if count in dictionary:
                dictionary[count].append(each)
            else:
                dictionary[count] = [each]
        return dictionary.values()


sol = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(sol.groupAnagrams(strs))
