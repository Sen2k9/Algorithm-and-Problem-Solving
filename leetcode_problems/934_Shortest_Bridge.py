"""
In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

Example 1:

Input: A = [[0,1],[1,0]]
Output: 1

Example 2:

Input: A = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:

Input: A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

Constraints:

    2 <= A.length == A[0].length <= 100
    A[i][j] == 0 or A[i][j] == 1
"""


from collections import deque


class Solution:
    def shortestBridge(self, A):

        # at first find two connected island using dfs
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        source, target, seen = self.findIsland(A)

        # use bfs to find the shortest path from source to target
        return self.shortestPath(source, target, seen)

    def findIsland(self, A):

        components = []

        seen = set()

        for r, row in enumerate(A):
            for c, val in enumerate(row):

                if val and (r, c) not in seen:
                    stack = []
                    seen_so_far = set()
                    stack.append((r, c))
                    seen_so_far.add((r, c))
                    seen.add((r, c))

                    while stack:
                        row, col = stack.pop()

                        for x, y in self.directions:
                            rx = row + x
                            cy = col + y

                            if rx >= 0 and rx <= len(A) - 1 and cy >= 0 and cy <= len(A[0]) - 1 and (rx, cy) not in seen and A[rx][cy] == 1:
                                stack.append((rx, cy))
                                seen.add((rx, cy))
                                seen_so_far.add((rx, cy))

                    components.append(seen_so_far)

        return components[0], components[1], seen

    def shortestPath(self, source, target, seen):

        queue = deque()
        for node in source:
            queue.append((node, 0))
        # print(queue)

        while queue:
            node, d = queue.popleft()

            for x, y in self.directions:
                rx = node[0] + x
                cy = node[1] + y

                if rx >= 0 and rx <= len(A) - 1 and cy >= 0 and cy <= len(A[0]) - 1:
                    if (rx, cy) in target:
                        return d

                    elif (rx, cy) not in seen:
                        seen.add((rx, cy))
                        new_node = (rx, cy)

                        queue.append((new_node, d+1))


sol = Solution()

A = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
print(sol.shortestBridge(A))

"""
what will happen if the array is very large?
"""
