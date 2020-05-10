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


class List:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000

        self.arr = [None]*self.size

    def add(self, key: int):

        index = key % self.size

        if not self.arr[index]:
            self.arr[index] = List(key, True)

        else:
            currHead = self.arr[index]

            while currHead.next:

                if currHead.key == key:
                    currHead.val = True
                    return

                currHead = currHead.next

            currHead.next = List(key, True)

    def remove(self, key: int):
        index = key % self.size

        if not self.arr[index]:
            return

        else:

            head = self.arr[index]

            while head:
                if head.key == key:
                    head.val = False
                    break

                head = head.next

    def contains(self, key: int):
        """
        Returns true if this set contains the specified element
        """
        index = key % self.size

        if not self.arr[index]:
            return False

        else:
            currHead = self.arr[index]

            while currHead:
                if currHead.key == key:
                    if currHead.val == True:
                        return True
                    else:
                        return False

                currHead = currHead.next

            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
#key = 2
obj.add(2)
obj.add(1)
print(obj.contains(1))
print(obj.contains(3))
obj.add(2)
print(obj.contains(2))
obj.remove(2)
print(obj.contains(2))
# obj.remove(key)
# param_3 = obj.contains(2)
# print(param_3)


# hashSet.add(1)
# hashSet.add(2)
# hashSet.contains(1)
# // returns true
# hashSet.contains(3)
# // returns false(not found)
# hashSet.add(2)
# hashSet.contains(2)
# // returns true
# hashSet.remove(2)
# hashSet.contains(2)
# // returns false(already removed)

"""
reference:
https://leetcode.com/problems/design-hashset/discuss/347478/Python-Solution-with-Chaining-without-boolean-array-(Explanation-included)
"""
