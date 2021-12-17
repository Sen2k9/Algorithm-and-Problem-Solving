from collections import defaultdict, deque


class Node:
    def __init__(self, val):
        self.val = val
        self.indegree = 0
        self.outdegree = 0


def is_scheduling_possible(tasks, prereq):
    adjacency_list = defaultdict(set)
    vertices = {}
    for u, v in prereq:
        if u not in vertices:
            u_node = Node(u)
            vertices[u] = u_node
        if v not in vertices:
            v_node = Node(v)
            vertices[v] = v_node
        u_node = vertices[u]
        v_node = vertices[v]
        v_node.indegree += 1
        u_node.outdegree += 1
        adjacency_list[u_node].add(v_node)
    visited = set()
    for vertex in range(tasks):
        if vertex in vertices \
            and not vertices[vertex].indegree \
                and vertex not in visited:
            queue = deque()
            queue.append(vertices[vertex])
            visited.add(vertex)
            while queue:
                node = queue.popleft()
                for child in adjacency_list[node]:
                    #print(child.val, child.indegree)
                    child.indegree -= 1
                    if child.indegree == 0:
                        queue.append(child)
                        visited.add(child.val)
            #print(visited)
    return sum(visited) == ((tasks - 1)*tasks)/2


def main():
    print("Is scheduling possible: " + str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " + str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " + str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))


main()
