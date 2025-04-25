"""
    A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.

 

Example 1:

Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"

Example 2:

Input: word = "unicornarihan"
Output: 0
Explanation: Not all 5 vowels are present, so there are no vowel substrings.

Example 3:

Input: word = "cuaieuouac"
Output: 7
Explanation: The vowel substrings of word are as follows (underlined):
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"

 

Constraints:

    1 <= word.length <= 100
    word consists of lowercase English letters only.


"""

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
        vowels = {"a", "e", "i", "o", "u"}

        last_seen_cons = -1
        last_seen_vowels = {v : -float("Inf") for v in vowels}
        ans = 0
        for idx, char in enumerate(word):

            if char not in vowels:
                last_seen_cons = idx
            
            else:
                last_seen_vowels[char] = idx
                ans += max(
                    min(last_seen_vowels.values()) - last_seen_cons,
                    0
                )
        
        return ans

                