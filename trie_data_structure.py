class TrieNode:
    def __init__(self):

        self.children = {}
        self.terminating = False


class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def getIndex(self, ch):
        return ord(ch) - ord("a")

    def insert(self, word):
        root = self.root
        for ch in word:
            index = self.getIndex(ch)
            if index not in root.children:
                new_root = self.getNode()
                root.children[index] = new_root
            root = root.children[index]

        root.terminating = True
        #print(word, root.terminating)

    def search(self, word):
        root = self.root

        for ch in word:
            index = self.getIndex(ch)
            if index not in root.children:
                return False
            root = root.children[index]

        #print(word, root.terminating)
        if root.terminating:
            return True
        else:
            return False

    def delete(self, word):
        root = self.root

        for ch in word:
            index = self.getIndex(ch)
            if index not in root.children:
                return False
            root = root.children[index]

        if root.terminating:
            root.terminating = False
            return True
        else:
            return False

    def update(self, old_word, new_word):
        if self.delete(old_word):

            self.insert(new_word)


if __name__ == "__main__":

    strings = ["pqrs", "pprt", "psst", "qqrs", "pqrs"]

    t = Trie()
    for word in strings:
        t.insert(word)

    print(t.search("pqrs"))
    print(t.search("pprt"))

    t.delete("pprt")

    print(t.search("pprt"))

    t.update("mnop", "pprt")
    print(t.search("pqrt"))

"""
references:
https://www.geeksforgeeks.org/trie-insert-and-search/
"""
