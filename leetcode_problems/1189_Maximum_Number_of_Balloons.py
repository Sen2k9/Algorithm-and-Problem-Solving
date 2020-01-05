"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:

Input: text = "nlaebolko"
Output: 1

Example 2:

Input: text = "loonbalxballpoon"
Output: 2

Example 3:

Input: text = "leetcode"
Output: 0

Constraints:

    1 <= text.length <= 10^4
    text consists of lower case English letters only.
"""


class Solution:
    def maxNumberOfBalloons(self, text: str):
        # Solution 1: self, using dictionary, horribly slow
        # if len(text) < 7:
        #     return 0
        # # "balloon"
        # dic = {}
        # dic["b"] = 0
        # dic["a"] = 0
        # dic["l"] = 0
        # dic["o"] = 0
        # dic["n"] = 0
        # count = 0

        # for each in text:
        #     dic[each] = dic.get(each, 0) + 1
        #     if dic["b"] >= 1 and dic["a"] >= 1 and dic["l"] >= 2 and dic["o"] >= 2 and dic["n"] >= 1:
        #         count += 1
        #         dic["b"] -= 1
        #         dic["a"] -= 1
        #         dic["l"] -= 2
        #         dic["o"] -= 2
        #         dic["n"] -= 1
        # # print(dic)
        # return count

        # Solution 2: using counter intelligently, faster

        # from collections import Counter

        # dic = Counter(text)  # O(n)
        # l = list("balloon")
        # output = 0
        # while True:
        #     if not l:
        #         output += 1
        #         l = list("balloon")
        #     key = l.pop()
        #     if dic.get(key, 0) == 0:
        #         break
        #     else:
        #         dic[key] -= 1
        # return output

        # Solution 3: fastest and optimize
        from collections import Counter
        counts = Counter(text)
        return min(
            counts['b'],
            counts['a'],
            counts['l'] // 2,
            counts['o'] // 2,
            counts['n']
        )


sol = Solution()
text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
print(sol.maxNumberOfBalloons(text))
"""
corner case:
1. text length at least 7

tips:
break out of a condition is faster than waiting to meet a condition ( see above two example)

reference:
https://leetcode.com/problems/maximum-number-of-balloons/discuss/383163/PythonPython3-Two-lines-using-a-Counter
"""
