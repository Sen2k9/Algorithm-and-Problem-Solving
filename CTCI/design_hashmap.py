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


import pdb


class LinkedList:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None


class MyHashMap:

    def __init__(self):
        self.a = [0] * 1000

    def put(self, key, val):
        index = key // 1000

        if self.a[index] == 0:
            self.a[index] = LinkedList(key, val)

        else:
            head = self.a[index]

            if head.key == key:
                head.val = val

            prev = head

            while head:

                if head.key == key:

                    head.val = val
                    return
                prev = head
                head = head.next

            prev.next = LinkedList(key, val)

    def get(self, k):
        index = k // 1000

        if self.a[index] == 0:
            return -1

        head = self.a[index]
        # if head.key == k:
        #     return head.val

        while head:
            if head.key == k:
                return head.val
            head = head.next
        return -1

    def remove(self, k):
        index = k // 10000

        if self.a[index] == 0:
            return
        head = self.a[index]
        if head.key == k:
            head = head.next
            return

        prev = head
        #nex = head.next

        while head:
            if head.key == k:
                prev.next = head.next
                return
            prev = head
            head = head.next


hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
assert hashMap.get(1) == 1

assert hashMap.get(3) == -1

hashMap.put(2, 1)
# print(hashMap.a[0])
# pdb.set_trace()
# print(hashMap.get(2))
assert hashMap.get(2) == 1
hashMap.remove(2)
assert hashMap.get(2) == -1
