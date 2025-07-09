"""
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

    LFUCache(int capacity) Initializes the object with the capacity of the data structure.
    int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
    void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.

To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3

 

Constraints:

    1 <= capacity <= 104
    0 <= key <= 105
    0 <= value <= 109
    At most 2 * 105 calls will be made to get and put.

    
"""

from collections import defaultdict

class ListNode:

    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next

class LinkedList:

    def __init__(self):
        # keeps left and right sentinel for LRU Cache
        self.left = ListNode(-1)
        self.right = ListNode(-1, self.left)
        self.left.next = self.right
        self.keyToNode = {} # key to ListNode map
    
    def pop(self, key):
        # mainly remove the node having key
        if key in self.keyToNode:
            curr = self.keyToNode[key] # get the node
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            del self.keyToNode[key]

    
    def pushRight(self, key):
        # push node at the end of doubly linked list to maintain LRU Cache
        node = ListNode(key, self.right.prev, self.right)
        self.keyToNode[key] = node

        self.right.prev = node
        node.prev.next = node


    def popleft(self):
        # remove specifically first node after left sentinel
        curr = self.left.next
        self.pop(curr.key)
        return curr
    

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.keyTocount = defaultdict(int) # frequency of each key
        self.lfuCnt = 1
        self.listMap = defaultdict(LinkedList) # frequency to doubly linkedlist map
        self.keyToVal = defaultdict(int) # key to val map

    def counter(self, key):
        cnt = self.keyTocount[key] # get the current count

        curr_list = self.listMap[cnt] # current doubly linked list

        # remove that key from that list as frequency changed
        curr_list.pop(key)
        self.keyTocount[key] += 1 # increment the count

        # assign that key to count + 1
        self.listMap[cnt + 1].pushRight(key)

        # if current count was lfu count and there is no node left after removing the current
        # update lfu count
        if cnt == self.lfuCnt and len(curr_list.keyToNode) == 0:
            self.lfuCnt = cnt + 1 # update the lfu

    def get(self, key: int) -> int:
        if key in self.keyToVal: # already exist
            self.counter(key) # increment the count
            return self.keyToVal[key]
        
        return -1

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key not in self.keyToVal and len(self.keyToVal) == self.cap:
            #evict
            evict_node = self.listMap[self.lfuCnt].popleft() # evict lru node for lfu doubly linkedlist
            del self.keyToVal[evict_node.key]
            del self.keyTocount[evict_node.key]

        self.keyToVal[key] = value
        self.counter(key) # increment count

        self.lfuCnt = min(self.lfuCnt, self.keyTocount[key])




# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

import unittest

class TestSuite(unittest.TestCase):
    
    def test_lfu_cache(self):
        obj = LFUCache(2)
        obj.put(1,1)
        
        self.assertEqual(
            obj.get(1),
            1
        )

if __name__ == "__main__":
    unittest.main()