"""
Build Order:
You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project).
All of a project's dependencies must be built before the project is.
Find a build order that will allow the projects to be built. If there is no valid build order, return an error.
"""
from collections import deque
from collections import defaultdict


class Node:

    def __init__(self, value):

        self.value = value
        self.indegree = 0
        self.outdegree = 0


class Graph:

    def __init__(self):
        self.projects = {}
        self.adjacency_list = {}

    def addProjects(self, value):
        if value not in self.projects:
            self.projects[value] = Node(value)
            self.adjacency_list[value] = set()

    def addDependencies(self, dependent, carier):

        if dependent not in self.projects or carier not in self.projects:
            return "Error"

        self.projects.get(dependent).outdegree += 1
        self.adjacency_list[dependent].add(self.projects.get(carier))
        self.projects.get(carier).indegree += 1


class Solution:

    def __init__(self):

        pass

    def buildOrder(self, graph):
        ans = []
        visited = set()  # O(n)
        for _, node in graph.projects.items():

            if node.indegree == 0 and node not in visited:

                # ans.append(node.value)
                visited.add(node)

                queue = deque()  # O(n)
                queue.append(node)
                while queue:
                    dependent = queue.popleft()

                    for each in graph.adjacency_list[dependent.value]:

                        each.indegree -= 1

                        if each.indegree == 0:
                            queue.append(each)
                            visited.add(each)

                    ans.append(dependent.value)

        return ans if len(ans) == len(graph.projects) else "Error"


projectGraph = Graph()

projectGraph.addProjects("a")
projectGraph.addProjects("b")
projectGraph.addProjects("c")
projectGraph.addProjects("d")
projectGraph.addProjects("e")
projectGraph.addProjects("f")

projectGraph.addDependencies("a", "d")
projectGraph.addDependencies("f", "b")
projectGraph.addDependencies("b", "f")
projectGraph.addDependencies("b", "d")
projectGraph.addDependencies("f", "a")
projectGraph.addDependencies("d", "c")

print(projectGraph.projects)

sol = Solution()
print(sol.buildOrder(projectGraph))


"""
complexity analysis:
Runtime : O(V+E)
"""
