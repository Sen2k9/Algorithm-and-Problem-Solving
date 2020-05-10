from heapq import *


def sort_k_messed_array(arr, k):
    # corner cases:
    if k == 0:
        return arr

    if len(arr) == 1:
        return arr

    minHeap = []
    j = 0

    for i in range(len(arr)):
        heappush(minHeap, arr[i])
        #print(minHeap, arr)

        if len(minHeap) > k:
            val = heappop(minHeap)

            arr[j] = val
            j += 1

        print(minHeap, arr)

    while minHeap:
        val = heappop(minHeap)
        arr[j] = val
        j += 1

    return arr


arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
k = 2
print(sort_k_messed_array(arr, k))

"""
K-Messed Array Sort

Given an array of integers arr where each element is at most k places away from its sorted position, code an efficient function sortKMessedArray that sorts arr. For instance, for an input array of size 10 and k = 2, an element belonging to index 6 in the sorted array will be located at either index 4, 5, 6, 7 or 8 in the input array.

Analyze the time and space complexities of your solution.

Example:

input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2

output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Constraints:

    [time limit] 5000ms

    [input] array.integer arr
        1 ≤ arr.length ≤ 100

    [input] integer k
        0 ≤ k ≤ 20

    [output] array.integer


"""
