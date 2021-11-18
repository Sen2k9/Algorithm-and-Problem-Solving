from collections import defaultdict, deque


class Vertex:

	def __init__(self, num):
		self.num = num
		self.indegree = 0
		self.outdegree = 0


def create_graph(edges: list, vertices: int):
    num_to_vertex_map = {}
    adjacency_list = defaultdict(list)
    for u, v in edges:
        #TODO: check vertices number is out of range or invalid
        if u not in num_to_vertex_map:
            num_to_vertex_map[u] = Vertex(u)
        num_to_vertex_map[u].outdegree += 1
        if v not in num_to_vertex_map:
            num_to_vertex_map[v] = Vertex(v)
        num_to_vertex_map[v].indegree += 1
        adjacency_list[num_to_vertex_map[u]].append(num_to_vertex_map[v])
    return (num_to_vertex_map, adjacency_list)


def topological_sort(edges: list, vertices: int):
	num_to_vertex_map, adjacency_list = create_graph(edges, vertices)
	visited = set()
	topological_order = []
	for vertex in range(vertices):
		curr = num_to_vertex_map[vertex]
		if curr.indegree == 0:
			queue = deque()
			queue.append(curr)
			visited.add(curr)
			while queue:
				curr = queue.popleft()
				topological_order.append(curr)
				for child in adjacency_list[curr]:
					if child not in visited:
						child.indegree -= 1
						if child.indegree == 0:
							queue.append(child)
							visited.add(child)
		
	return output(topological_order)

def output(topological_order: list):
	# output answer as user wants
	return [vertex.num for vertex in topological_order]


import unittest

class TestSolution(unittest.TestCase):

	def test_topological_sort(self):
		self.assertIn(topological_sort([[3, 2], [3, 0], [2, 0], [2, 1]], 4),[[3, 2, 0, 1], [3, 2, 1, 0]])
        #self.assertIn(topological_sort([[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]], 5),[[4, 2, 3, 0, 1],[4, 3, 2, 0, 1],[4, 3, 2, 1, 0],[4, 2, 3, 1, 0],[4, 2, 0, 3, 1]])

if __name__ == '__main__':
		unittest.main()
