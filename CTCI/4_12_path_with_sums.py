"""
Paths with Sum:
You are given a binary tree in which each node contains an integer value (which might be positive or negative).
Design an algorithm to count the number of paths that sum to a given value. The path does not need to start or end at the root or a leaf,
but it must go downwards (travelling only from parent nodes to child nodes).
"""


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BT:

    def __init__(self):
        pass

    def makeTree(self, arr):

        if not arr:
            return None

        if len(arr) == 1:
            return Node(arr[0])

        mid = len(arr) // 2

        root = Node(arr[mid])

        left = self.makeTree(arr[:mid])

        right = self.makeTree(arr[mid + 1:])

        root.left = left
        root.right = right

        return root


class Solution:

    def __init__(self):
        pass

    def path_with_sum(self, root, target):

        hashMap = {}

        return self.countPaths(root, target, 0, hashMap)

    def countPaths(self, root, target, runningSum, hashMap):

        if not root:
            return 0

        runningSum += root.val

        residue = runningSum - target

        totalPath = hashMap.get(residue, 0)

        if runningSum == target:
            totalPath += 1

        self.incrementHashMap(runningSum, hashMap, 1)

        totalPath += self.countPaths(root.left, target, runningSum, hashMap)
        totalPath += self.countPaths(root.right, target, runningSum, hashMap)

        self.incrementHashMap(runningSum, hashMap, -1)

        return totalPath

    def incrementHashMap(self, runningSum, hashMap, delta):

        newCount = hashMap.get(runningSum, 0) + delta

        if newCount == 0:
            del hashMap[runningSum]

        else:

            hashMap[runningSum] = newCount


if __name__ == '__main__':

    binaryTree = BT()
    root = binaryTree.makeTree([3, 3, -2, 5, 1, 2, 10, -3, 11])

    sol = Solution()

    print(sol.path_with_sum(root, 8))
