class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.islastNode = False


class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def getIndex(self, ch):
        return ord(ch) - ord("a")

    def __insert__(self, key):

        current = self.root

        for each in key:
            index = self.getIndex(each)

            if not current.children[index]:
                current.children[index] = self.getNode()
            current = current.children[index]

        current.islastNode = True

    def __search__(self, key):
        current = self.root

        for each in key:
            index = self.getIndex(each)

            if not current.children[index]:
                return False

            current = current.children[index]

        return current.islastNode and current != None


# driver function
def main():

    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.__insert__(key)

    # Search for different keys
    print("{} ---- {}".format("the", output[t.__search__("the")]))
    print("{} ---- {}".format("these", output[t.__search__("these")]))
    print("{} ---- {}".format("their", output[t.__search__("their")]))
    print("{} ---- {}".format("thaw", output[t.__search__("thaw")]))


if __name__ == '__main__':
    main()

"""
references:
https://www.geeksforgeeks.org/trie-insert-and-search/
"""
