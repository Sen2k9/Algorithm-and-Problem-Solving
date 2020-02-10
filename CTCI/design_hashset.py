"""
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

    add(value): Insert a value into the HashSet. 
    contains(value) : Return whether the value exists in the HashSet or not.
    remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.


Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)


Note:

    All values will be in the range of [0, 1000000].
    The number of operations will be in the range of [1, 10000].
    Please do not use the built-in HashSet library.

"""


class LinkedList:
    def __init__(self, k):
        self.key = k
        self.next = None


class MyHashSet:

    def __init__(self):
        self.a = [0] * 1000

    def add(self, k):
        index = k // 1000
        if self.a[index] == 0:
            self.a[index] = LinkedList(k)

        else:
            head = self.a[index]
            prev = head

            while head:
                if head.key == k:
                    return
                prev = head
                head = head.next
            prev.next = LinkedList(k)

    def contains(self, key):
        index = key // 1000

        if self.a[index] == 0:
            return False

        else:
            head = self.a[index]
            while head:
                if head.key == key:
                    return True
                #prev = head
                head = head.next

        return False

    def remove(self, key):
        index = key // 1000

        if self.a[index] == 0:
            return
        else:
            head = self.a[index]
            prev = head
            while head:
                if head.key == key:
                    prev.next = head.next
                    return

                prev = head
                head = head.next


hashSet = MyHashSet()
hashSet.add(1)
hashSet.add(2)
assert hashSet.contains(1) == True
assert hashSet.contains(3) == False
hashSet.add(2)
print(hashSet.contains(2))
assert hashSet.contains(2) == True
hashSet.remove(2)
assert hashSet.contains(2) == False
