class Solution:

    def permutation(self, s):
        self.l = []
        self.do_permutation(s, "", self.l)
        return self.l

    def do_permutation(self, s, prefix, l):
        if len(s) == 0:
            self.l.append(prefix)  # O(n!) runtime
            return
        else:
            for i in range(len(s)):  # for each n runs n! times > O(n*n!)
                rem = s[0:i] + s[i + 1:]
                # string concatenation takes O(n) time
                self.do_permutation(rem, prefix + s[i], self.l)


"""
total runtime:
base case: O(n!)

else loop:
    O(n*(n*n!)) = O(n^2*n!)
total = base case + else loop = O(n!) + O(n^2*n!)
"""

sol = Solution()
s = "ABCD"
print(sol.permutation(s))
