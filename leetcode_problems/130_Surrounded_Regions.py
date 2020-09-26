"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:

Surrounded regions shouldn’t be on the border, 
which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # optimal solution
        if not board:
            return
        row_length = len(board)
        col_length = len(board[0])

        # corner case
        if row_length == 1 or col_length == 1:
            return

        visited = set() # O(N) space complexity
        # top row, bottom row
        for row in [0, row_length - 1]:
            for col, val in enumerate(board[row]):

                if val == 'O':
                    board[row][col] = "1"
                    visited.add((row, col))
                    self.dfs_lookup(row, col, board, visited)
        
        # first column, last column
        for col in [0, col_length -1]:
            for row_index in range(row_length):

                if board[row_index][col] == 'O' and (row_index, col) not in visited:
                    board[row_index][col] = "1"
                    visited.add((row, col))
                    self.dfs_lookup(row_index, col, board, visited)
        
        # all marked "1" is can not flipped so change back to "o"
        # all non marked "o" represents they are not accesible from the border
        # So they can be flipped to "X"
        print(board)
        for row_i in range(len(board)):
            for col_j in range(len(board[0])):

                if board[row_i][col_j] == "1":

                    board[row_i][col_j] = 'O'
                
                elif board[row_i][col_j] == 'O':

                    board[row_i][col_j] = "X"

        print(board, visited)





    def dfs_lookup(self, row, col, board, visited):

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        for row_i, col_j in directions:
            new_row = row_i + row
            new_col = col_j + col
            #print(new_row, new_col)

            if 0 <= new_row < len(board) \
               and 0 <= new_col < len(board[0]) \
               and board[new_row][new_col] == 'O' \
               and (new_row, new_col) not in visited:
               

               board[new_row][new_col] = "1"

               visited.add((new_row, new_col))

               self.dfs_lookup(new_row, new_col, board, visited)


sol = Solution()
board = [
    ["X", "X", "X", "X"],
    ["X", 'O', 'O', "X"],
    ["X", "X", 'O', "X"],
    ["X", 'O', "X", "X"],
]

print(sol.solve(board))

# row matrix
board = [
    ["X", "X", "X", "X"]
]
print(sol.solve(board))

# column matrix
board = [
    ["X"], ["X"], ["X"], ["X"]
]
print(sol.solve(board))


board = [
    ["X", "X", "X", "X", "X"],
    ["X", "X", 'O', "X", "X"],
    ["X", 'O', "X", 'O', "X"],
    ["X", 'O', "X", "X", "X"],
]

print(sol.solve(board))


"""
Runtime Complexity: O(N), traverse the whole matrix in-place
Space Complexity : O(N), stored visited index 
"""