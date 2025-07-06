"""
Given two strings s1 and s2, return true if s2 contains a

of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false



Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.


"""
import unittest

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Count = {} # frequency count
        matched = 0
        # get count of all character in s1
        for char in s1:
            s1Count[char] = s1Count.get(char, 0) + 1
        
        # run sliding window method
        for idx in range(len(s2)):
            curr = s2[idx]
            # if there is a match, update matched count
            if  curr in s1Count:
                s1Count[curr] -= 1
                if s1Count[curr] == 0:
                    matched += 1
            
            # matched valued out of sliding window, so decrease the match
            if idx >= len(s1) and s2[idx - len(s1)] in s1Count:
                # removed from match if the character out of window was included
                if s1Count[s2[idx - len(s1)]] == 0:
                    matched -= 1
                s1Count[s2[idx - len(s1)]] += 1


            # got all matched
            if matched == len(s1Count):
                return True
        
        return False
    

class TestSuite(unittest.TestCase):
    
    def test_checkInclusion(self):
        sol = Solution()
        s1 = "ab"
        s2 = "eidbaooo"
        
        self.assertEqual(
            sol.checkInclusion(
                s1, s2
            ),
            True
        )
        
if __name__ == "__main__":
    unittest.main()
