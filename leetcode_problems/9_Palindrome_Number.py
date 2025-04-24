"""
    Given an integer x, return true if x is a

, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 

Constraints:

    -231 <= x <= 231 - 1

 
Follow up: Could you solve it without converting the integer to a string?
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        def check_palindrome(s, l, r):
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    return False
                l -= 1
                r += 1
            return True
        
        num_str = str(x)

        if len(num_str) % 2 == 0:
            return check_palindrome(num_str, len(num_str)// 2 - 1, len(num_str)//2)
        
        return check_palindrome(num_str, len(num_str)// 2 , len(num_str)//2)