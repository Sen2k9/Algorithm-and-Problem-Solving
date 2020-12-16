'''
procedure dfs(G)

for v in V:
    visited(v) = False

for v in V:
    if not visited(v):
        explore(v) # look for Figure 3.3. for pseudocode
'''


class Solution:

    def __init__(self):
        self.vertices = []  # list of vertices
        self.edges = {}  # adjacency list

    def dfs(self):

        self.visited = set()

        for v in self.vertices:  # traverse all vertex one by one
            if v not in self.visited:
                self.explore(v)

    def explore(self, vertex):
        '''
        recursively traverse all the child of a current node
        '''

        self.visited.add(vertex)

        self.previsit(vertex)

        for child in self.edges[vertex]:
            if child not in self.visited:
                self.explore(child)

        self.postvisit(vertex)

    def previsit(self, vertex):
        pass

    def postvisit(self, vertex):
        pass
