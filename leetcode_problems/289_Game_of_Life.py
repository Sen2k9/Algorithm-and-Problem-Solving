"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

Follow up:

    Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
    In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

"""


class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        check = [(-1, 0), (1, 0), (0, -1), (0, 1),
                 (-1, -1), (1, 1), (-1, 1), (1, -1)]
        changes = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                life = board[i][j]
                count = 0
                for k, l in check:
                    new_i = i+k
                    new_j = j+l
                    if new_i >= 0 and new_i <= len(board)-1 and new_j >= 0 and new_j <= len(board[0])-1:
                        if board[new_i][new_j] == 1:
                            count += 1
                #print(i, j, life, count)

                if life == 1:
                    if count < 2:  # under-population
                        changes.append([(i, j), 0])
                    elif count > 3:
                        changes.append([(i, j), 0])
                else:
                    if count == 3:
                        changes.append([(i, j), 1])

        for each in changes:
            i = each[0][0]
            j = each[0][1]

            value = each[1]

            board[i][j] = value
        # print(changes)
        return board


sol = Solution()
board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]
print(sol.gameOfLife(board))

"""
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

"""
