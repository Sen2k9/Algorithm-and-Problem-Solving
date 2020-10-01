"""
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

Example 1:

Input: graph = [
  [1,1,0],
  [0,1,0],
  [1,1,1]
]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

Example 2:

Input: graph = [
  [1,0,1],
  [1,1,0],
  [0,1,1]
]
Output: -1
Explanation: There is no celebrity.

Note:

    The directed graph is represented as an adjacency matrix, which is an n x n matrix where a[i][j] = 1 means person i knows person j while a[i][j] = 0 means the contrary.
    Remember that you won't have direct access to the adjacency matrix.

"""


# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
from collections import defaultdict
from functools import lru_cache


class Solution:

    def __init__(self):
        self.adjacency_matrix = defaultdict(set)
    
    def findCelebrity(self, n: int) -> int:
        celebrity_candidate = 0

        # first to find out celebrity candidate
        for i in range(1, n):
            if self.cache_knows(celebrity_candidate, i):
                celebrity_candidate = i
        
        # exhaustive check whether the candidate is the celebrity
        if self.isCelebrity(celebrity_candidate):
            return celebrity_candidate

        return -1

    def isCelebrity(self, candidate):

        for i in range(n):
            print(i, candidate)
            if i == candidate:
                continue

            if self.cache_knows(candidate, i) or not self.cache_knows(i, candidate):
                return False

        return True

    @lru_cache
    def cache_knows(self, a, b):
        return self.knows(a, b)

    def knows(self, a: int, b: int):

        if b in self.adjacency_matrix[a]:
            return True
        return False

    def adjacency(self, graph):

        for i in range(len(graph)):
            for j in range(len(graph[0])):

                if i == j:
                    continue

                if graph[i][j] == 1:
                    self.adjacency_matrix[i].add(j)

        print(self.adjacency_matrix)



sol = Solution()
graph = [
  [1,1,0],
  [0,1,0],
  [1,1,1]
]
n = 3
sol.adjacency(graph)
print(sol.findCelebrity(n))

sol = Solution()
graph = [[1,0],[0,1]]
n = 2
sol.adjacency(graph)
print(sol.findCelebrity(n))

sol = Solution()
graph = [[1,0],[1,1]]
n = 2
sol.adjacency(graph)
print(sol.findCelebrity(n))

sol = Solution()
graph = [[1,0,1],[1,1,0],[0,1,1]]
n = 3
sol.adjacency(graph)
print(sol.findCelebrity(n))
