'''
procedure explore(G,v)
Input: G = (V, E) is a graph; v elements of set V
Output: visited(u) is set to true for all nodes u reachable from v

Algorithm:

visited(v) = True
previsit(v)

for each edge (v,u) in E:
    if not visited(u):
        explore(u)

postvisit(v)
'''


class Solution:

    def __init_(self):
        self.neighbours = {}

    def explore(self, G, v):

        self.visited = set()

        self.visited.add(v)

        self.previsit(v)

        for u in self.neighbours[v]:
            if u not in self.visited:
                self.explore(u)

        self.postvisit(v)

    def previsit(self, v):
        pass

    def postvisit(self, v):
        pass
