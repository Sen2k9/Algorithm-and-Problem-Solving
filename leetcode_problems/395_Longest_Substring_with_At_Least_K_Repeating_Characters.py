"""
 Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input:
s = "ababbc", k = 2

Output:
5
The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""
from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k < 2:
            return len(s)
        if not s or len(s) < k:
            return 0

        print(s)
        char_count = Counter(s)
        print(char_count)
        mid = 0
        end = len(s) - 1

        second_half = 0
        while mid <= end:
            if char_count[s[mid]] < k:
                print(mid)
                break
            mid += 1

        if mid == len(s):
            return mid
        
        # potential substring
        first_half = self.longestSubstring(s[:mid], k)

        while mid <= end and char_count[s[mid]] < k:
            mid += 1

        # potential substring
        second_half = self.longestSubstring(s[mid:], k) if mid < len(s) else 0

        return max(first_half, second_half)


sol = Solution()
s = "ababbc"
k = 2
print(sol.longestSubstring(s, k))

s = "aaabb"
k = 3
print(sol.longestSubstring(s, k))

s = "aaabbb"
k = 3
print(sol.longestSubstring(s, k))

s = "ababacb"
k = 3
print(sol.longestSubstring(s, k))