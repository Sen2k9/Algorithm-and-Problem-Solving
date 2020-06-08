"""
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
"""

"""
clarifying questions:
1. As it is a graph, is there any cycle?
2. Graph can constitute single node?
3. Can I expect to have one singly connected tree?

"""


# creating the structure




import unittest
from collections import deque
from collections import defaultdict
class Graph:

    def __init__(self):
        self.vertices = set()

        self.adjacency_list = {}

    def addEdge(self, fromNode, toNode):

        if fromNode not in self.adjacency_list:
            self.adjacency_list[fromNode] = {toNode}

        else:
            self.adjacency_list[fromNode].add(toNode)

    def addVertices(self, node):
        self.vertices.add(node)

    def getVertices(self, node):
        if node in self.vertices:
            return node

# api


def route_between_nodes(graph, fromNode, toNode) -> bool:

    if fromNode == toNode:
        return False

    elif fromNode not in graph.vertices or toNode not in graph.vertices:
        return False

    queue = deque()
    queue.append(fromNode)

    while queue:
        length = len(queue)

        for _ in range(length):

            node = queue.popleft()

            if node == toNode:
                return True

            if node in graph.adjacency_list:
                for child in graph.adjacency_list[node]:
                    queue.append(child)

# test code


class TestRoute(unittest.TestCase):

    def test_route_betweee_nodes(self):

        # creating test cases
        graph = Graph()
        graph.addVertices(1)

        graph.addVertices(2)

        graph.addVertices(3)

        graph.addVertices(4)

        graph.addVertices(5)

        graph.addVertices(6)

        graph.addEdge(1, 2)

        graph.addEdge(1, 3)

        graph.addEdge(1, 4)

        graph.addEdge(3, 5)

        graph.addEdge(3, 6)

        self.assertEqual(route_between_nodes(graph, graph.getVertices(
            1), graph.getVertices(6)), True)

        self.assertEqual(route_between_nodes(graph, 1, 1), False)


# it means if we run this script then the below code will execute
# but if we import this module the below code will get skipped
if __name__ == '__main__':

    unittest.main()

"""
https://stackoverflow.com/questions/20992731/meaning-of-unittest-main-in-python-unittest-module
"""
