"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]

Example 2:

Input: 5
Output: [0,1,1,2,1,2]

Follow up:

    It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
    Space complexity should be O(n).
    Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

"""


class Solution:
    def countBits(self, num: int):
        # Solution 1: brute-force
        # ans = []
        # for i in range(num + 1):
        #     ones = bin(i).split("0b")[1].count("1")
        #     ans.append(ones)
        # return ans

        # Solution 2: using dictionary
        # dic = {0: 0, 1: 1}
        # ans = []
        # for i in range(num + 1):
        #     div = i // 2
        #     mod = i % 2
        #     if mod == 1:
        #         dic[i] = dic[div] + 1
        #     else:
        #         dic[i] = dic[div]
        #     ans.append(dic[i])

        # return ans

        # Solution 3: efficient, using dynamic programming
        if num == 0:
            return [0]

        ans = [0, 1]

        for i in range(2, num + 1):
            if i % 2 == 0:
                ans.append(ans[i // 2])
            else:
                ans.append(ans[i // 2] + 1)

        return ans


sol = Solution()
num = 15
print(sol.countBits(num))
