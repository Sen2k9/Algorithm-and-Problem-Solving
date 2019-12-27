"""
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

    put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
    get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
    remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.


Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);
hashMap.put(2, 2);
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found)


Note:

    All keys and values will be in the range of [0, 1000000].
    The number of operations will be in the range of [1, 10000].
    Please do not use the built-in HashMap library.


"""
# Solution 1: self


# class MyHashMap:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.key = []
#         self.value = []

#     def put(self, key: int, value: int):
#         """
#         value will always be non-negative.
#         """
#         if key in self.key:
#             index = self.key.index(key)
#             self.value[index] = value
#         else:
#             self.key.append(key)
#             self.value.append(value)

#     def get(self, key: int):
#         """
#         Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
#         """
#         if key in self.key:
#             index = self.key.index(key)
#             return self.value[index]
#         else:
#             return -1

#     def remove(self, key: int):
#         """
#         Removes the mapping of the specified value key if this map contains a mapping for the key
#         """
#         if key in self.key:
#             index = self.key.index(key)
#             del self.value[index]
#             del self.key[index]

# Solution 2: Faster, using Linked List
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.hashMap = [None]*self.size

    def put(self, key: int, value: int):
        """
        value will always be non-negative.
        """
        index = key % self.size

        if self.hashMap[index] == None:
            self.hashMap[index] = ListNode(key, value)
        else:
            curr_node = self.hashMap[index]
            while True:

                if curr_node.key == key:
                    curr_node.value = value
                    return

                if curr_node.next == None:
                    break
                curr_node = curr_node.next
            curr_node.next = ListNode(key, value)

    def get(self, key: int):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size

        cur_node = self.hashMap[index]
        while cur_node:
            if cur_node.key == key:
                return cur_node.value
            else:
                cur_node = cur_node.next
        return -1

    def remove(self, key: int):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size
        cur_node = prev_node = self.hashMap[index]
        if not cur_node:
            return
        if cur_node.key == key:
            self.hashMap[index] = cur_node.next
        else:
            cur_node = cur_node.next
            while cur_node:
                if cur_node.key == key:
                    prev_node.next = cur_node.next
                    break
                prev_node, cur_node = cur_node, cur_node.next


# Your MyHashMap object will be instantiated and called as such:
key = 1
value = 2
obj = MyHashMap()
obj.put(key, value)
param_2 = obj.get(key)
obj.remove(key)
print(param_2)
print(obj.get(key))
"""
references:
https://leetcode.com/problems/design-hashmap/discuss/310257/Open-Hashing-Python-Solution-with-detailed-explanation
"""
