"""
Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain.

Example 1:

Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too. 
The sister has three different kinds of candies. 

Example 2:

Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1]. 
The sister has two different kinds of candies, the brother has only one kind of candies. 

Note:

    The length of the given array is in range [2, 10,000], and will be even.
    The number in given array is in range [-100,000, 100,000].
"""


class Solution:
    def distributeCandies(self, candies):
        # Solution 1: self, fastest
        c = set(candies)
        sis = len(candies) // 2
        return min(len(c), sis)
        
        # you can save space if you do not assign intermediate result to any variables like below
        # return min(len(set(candies)), len(candies)//2)

        # Solution 2: using dictionary, slower
        # dic = {}
        # for each in candies:
        #     dic[each] = dic.get(each, 0) + 1
        # return min(len(dic.keys()), len(candies) // 2)
        
        # Solution 3: using counter

        # import collections
        # dic = collections.Counter(candies)

        # return min(len(dic.keys()),len(candies)//2)





sol = Solution()
candies = [1,2,3,4]
print(sol.distributeCandies(candies))
"""
corner case:
[1,2,3,4]
[1,1,1,2]
"""