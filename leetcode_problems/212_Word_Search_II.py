class Solution:

    def findWords(self, board, words):
        self.trie = Trie()
        self.ans = set()
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for word in words:
            self.trie.addWord(word)
        row_length = len(board)
        col_length = len(board[0])
        for r in range(row_length):
            for c in range(col_length):
                #print(r, c)
                curr_char = board[r][c]
                # start a new visited set for each starting point
                if self.trie.head.children.get(curr_char, None):
                    self.traverse(self.trie.head, curr_char, r, c, board)
        return list(self.ans)

    def traverse(self, curr_node, curr_char, r, c, board):
        #print(curr_char, r, c)
        #print(visited)
        #print(self.ans)
        
        new_node= curr_node.children.get(curr_char, None)
        if not new_node:
            return False
        # char does not exist in children
        if new_node.isWord:
            self.ans.add(new_node.isWord)
        board[r][c] = '#'
        for i, j in self.directions:
            new_row = i + r
            new_col = j + c
            if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
                new_char = board[new_row][new_col]
                self.traverse(new_node, new_char, new_row, new_col, board)
        board[r][c] = curr_char
        return False


class TrieNode:
    
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isWord = False
        
class Trie:
    
    def __init__(self):
        self.head = TrieNode("0")

    def addWord(self, word):
        curr = self.head
        for char in word:
            if not curr.children.get(char, None):
                curr.children[char] = TrieNode(char)
            curr = curr.children.get(char)
        curr.isWord = word

    def searchWord(self, char, curr_node):
        if not curr_node.children.get(char, None):
            return False
        elif curr_node.children[char].val != char:
            return False
        else:
            return curr_node.children.get(char)


board = [["a","b"],["c","d"]]
words = ["abcb"]
sol = Solution()
print(sol.findWords(board, words))

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
sol = Solution()
print(sol.findWords(board, words))

board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
words = ["oa","oaa"]
sol = Solution()
print(sol.findWords(board, words))
board = [["a","a"]]
words = ["aaa"]
sol = Solution()
print(sol.findWords(board, words))

board = [["a","b","c","e"],["x","x","c","d"],["x","x","b","a"]]
words = ["abc","abcd"]
sol = Solution()
print(sol.findWords(board, words))

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain","hklf", "hf"]
sol = Solution()
print(sol.findWords(board, words))