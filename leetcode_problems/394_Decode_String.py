"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

"""
import unittest

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for idx in range(len(s)):

            if s[idx] != "]":
                stack.append(s[idx])
            
            else:
                substr = ""
                # capture all the words
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                
                # pop [
                stack.pop()

                k = ""
                # capture all the digits
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(int(k) * substr)
        
        return "".join(stack)


class TestSuite(unittest.TestCase):
    
    def test_decode_string(self):
        sol = Solution()
        s = "3[a]2[bc]"
        self.assertEqual(
            sol.decodeString(s),
            "aaabcbc"
        )
        s = "3[a2[c]]"
        self.assertEqual(
            sol.decodeString(s),
            "accaccacc"
        )

if __name__ == "__main__":
    unittest.main()

"""
references:
https://leetcode.com/problems/decode-string/discuss/459263/Easy-to-understand-Python-Stack-solution
"""
