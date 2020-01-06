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


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.m = [None]*self.size

    def add(self, key: int):
        index = key % self.size
        # If the node at given index is None then set it with given key
        if self.m[index] == None:
            self.m[index] = ListNode(key, True)
        else:
            currNode = self.m[index]
            # If there are nodes at given index then traverse the linked-list and attach the key at the end.
            tempHead = currNode
            self.m[index] = ListNode(key, True)
            self.m[index].next = currNode

    def remove(self, key: int):
        index = key % self.size
        # If node at given index is None then do nothing.
        if self.m[index] == None:
            return
        # Otherwise find given key in the linked-list at current index and set its value to False.
        else:
            currNode = self.m[index]
            while currNode:
                if currNode.key == key:
                    currNode.val = False
                    break
                currNode = currNode.next

    def contains(self, key: int):
        """
        Returns true if this set contains the specified element
        """
        index = key % self.size
        # If there's no linked-list at given index then return False.
        if self.m[index] == None:
            return False
        # Otherwise traverse the linked-list to check if the desired element is present and its value is True.
        else:
            currNode = self.m[index]
            while currNode:
                if currNode.key == key:
                    if currNode.val == True:
                        return True
                    else:
                        return False
                currNode = currNode.next
            return False


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
