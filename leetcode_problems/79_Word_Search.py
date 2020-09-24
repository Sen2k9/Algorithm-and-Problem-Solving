"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

Constraints:

    board and word consists only of lowercase and uppercase English letters.
    1 <= board.length <= 200
    1 <= board[i].length <= 200
    1 <= word.length <= 10^3

"""


class Solution:
    def exist(self, board, word: str):

        # Solution 1: brute-force
        # O(mn)
        for row_index, rows in enumerate(board):
            for col_index, column in enumerate(rows):
                seen_cells = []
                # we only interested to check cells for one path
                if board[row_index][col_index] == word[0]:
                    # store the cell so that it does not use more than onece.
                    seen_cells.append((row_index, col_index))
                    if self.word_exist(row_index, col_index, board, word[1:], seen_cells):
                        return True
                    #print(seen_cells)    
        return False

    def word_exist(self, row, col, board, word, seen_cells):
        #print(seen_cells)    
        if len(word) == 0:
            return True
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for row_i, col_i in directions:
            new_row = row + row_i
            new_col = col + col_i
            if 0 <= new_row < len(board) and \
               0 <= new_col < len(board[0]) and \
               (new_row, new_col) not in seen_cells and \
               board[new_row][new_col] == word[0]:
                seen_cells.append((new_row, new_col))
                if self.word_exist(new_row, new_col, board, word[1:], seen_cells):
                    return True
                seen_cells.pop()
        return False


sol = Solution()
board = [
    ["A","B","C","E"],
    ["S","F","E","S"],
    ["A","D","E","E"]]

word = "ABCESEEEFS"
print(sol.exist(board, word))
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
print(sol.exist(board, word))
word = "ABCB"
print(sol.exist(board, word))
word = "SEE"
print(sol.exist(board, word))

"""
Note: Although the problem seems use dfs. 
It is kind of backtracking, taking into account the dfs processes.

Tricky time and space complexity analysis.

Time Comlexity:
1. Think about what is happening for every cell, when you want to match the word.
2. We are travelling in four direction only for the first match.
3. After that, we only travel three directions.
4. We don't travel again to the direction we are going. 
So it lefts three directions.
5. For worst case (where we exhaust the board to search for a word),
we go every three direction for each cell and the length of traversing is the length of the word given.
6. So, for N cells we go 3^L, where L is the word size, makes it O(N.3^L)

Space Complexity:
1. We store the cell value as most the word length. Also same for recursion steps.
2. So, we basically use L blocks of memory, which makes it O(L).
"""