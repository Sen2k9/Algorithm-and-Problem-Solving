class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        first_ptr = 0
        second_ptr = 0
        ans = 0

        # traverse the first pointer one by one to compare with the target string
        while first_ptr < len(s): # go through the given string
            char = s[first_ptr : second_ptr+1] # take substring
            # compare the subtring with equal length of each posible substring of the target string
            ans += self.compare(char, len(char), t)

            # increment second pointer one by one
            second_ptr += 1

            # if second pointer reach the string length, then we are finish
            # increment first pointer to the next character
            if second_ptr == len(s): 
                first_ptr += 1
                second_ptr = first_ptr

        return ans

    def compare(self, substring, length, target):
        """
        this function returns the number of "exactly one character difference"
        between the given substring

        """
        i = 0
        ans = 0
        # traverse through the target string
        while i < len(target) - length + 1:
            no_match = 0

            for index in range(length):
                if substring[index] != target[i+index]:
                    no_match += 1

                # no need to traverse if more than one character mismatch
                if no_match > 1:
                    break

            if no_match == 1:
                ans += 1
            i += 1

        return ans

        


sol = Solution()
s = "abe"
t = "bbc"
print(sol.countSubstrings(s,t))

s = "aba"; t = "baba"
print(sol.countSubstrings(s,t))

s = "ab"; t = "bb"
print(sol.countSubstrings(s,t))

s = "a"; t = "a"
print(sol.countSubstrings(s,t))
