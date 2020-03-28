"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

 

Constraints:

    The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.
    1 <= numCourses <= 10^5
"""


class Graph:
    def __init__(self):
        self.indegre = 0
        self.outedge = []


class Solution:
    def canFinish(self, numCourses, prerequisites):
        from collections import defaultdict, deque
        graph = defaultdict(Graph)
        total_edge = 0

        for each in prerequisites:
            nextcourse = each[0]
            prevcourse = each[1]
            graph[prevcourse].outedge.append(nextcourse)
            graph[nextcourse].indegre += 1
            total_edge += 1

        nodepvertex = deque()

        for vertex, _ in graph.items():
            if graph[vertex].indegre == 0:
                nodepvertex.append(vertex)

        removeEdge = 0
        while nodepvertex:
            course = nodepvertex.popleft()
            for nextcourse in graph[course].outedge:
                graph[nextcourse].indegre -= 1
                removeEdge += 1
                if graph[nextcourse].indegre == 0:
                    nodepvertex.append(nextcourse)

        if removeEdge == total_edge:
            return True
        else:
            False


sol = Solution()
n = 3
pre = [[1, 0], [2, 0]]
print(sol.canFinish(n, pre))
