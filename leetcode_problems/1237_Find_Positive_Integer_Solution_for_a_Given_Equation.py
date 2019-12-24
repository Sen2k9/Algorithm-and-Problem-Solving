"""
Given a function  f(x, y) and a value z, return all positive integer pairs x and y where f(x,y) == z.

The function is constantly increasing, i.e.:

    f(x, y) < f(x + 1, y)
    f(x, y) < f(x, y + 1)

The function interface is defined like this: 

interface CustomFunction {
public:
  // Returns positive integer f(x, y) for any given positive integer x and y.
  int f(int x, int y);
};

For custom testing purposes you're given an integer function_id and a target z as input, where function_id represent one function from an secret internal list, on the examples you'll know only two functions from the list.  

You may return the solutions in any order.

 

Example 1:

Input: function_id = 1, z = 5
Output: [[1,4],[2,3],[3,2],[4,1]]
Explanation: function_id = 1 means that f(x, y) = x + y

Example 2:

Input: function_id = 2, z = 5
Output: [[1,5],[5,1]]
Explanation: function_id = 2 means that f(x, y) = x * y

 

Constraints:

    1 <= function_id <= 9
    1 <= z <= 100
    It's guaranteed that the solutions of f(x, y) == z will be on the range 1 <= x, y <= 1000
    It's also guaranteed that f(x, y) will fit in 32 bit signed integer if 1 <= x, y <= 1000


"""
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""


class Solution:

    def findSolution(self, customfunction, z):
        # Solution 1: Brute-force
        # A = []
        # for x in range(1, z + 1):
        #     if customfunction.f(x, 1) > z:
        #         return A
        #     for y in range(1, z + 1):
        #         if customfunction.f(x, y) == z:
        #             A.append([x, y])
        #             break
        # return A

        # Solution 2: Using binary Search
        A = []
        for x in range(1, z + 1):
            if customfunction.f(x, 1) > z:
                return A
            a, b = 1, z
            while a < z + 1:
                mid = (a + b) // 2
                print(a, b)
                print(mid)
                if customfunction.f(x, mid) > z:
                    b = mid-1
                elif customfunction.f(x, mid) < z:
                    a = mid+1
                if customfunction.f(x, mid) == z:
                    A.append([x, mid])
                    break
                if a > b:
                    break
        return A


class CustomFunction:
    def f(self, x, y):
        return x+y


sol = Solution()
z = 5
c = CustomFunction()
print(sol.findSolution(c, z))
"""
reference:
https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/discuss/414196/Two-Solutions-in-Python-3-(beats-100)
"""
