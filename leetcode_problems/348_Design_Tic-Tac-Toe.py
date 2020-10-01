"""
Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

    A move is guaranteed to be valid and is placed on an empty block.
    Once a winning condition is reached, no more moves are allowed.
    A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

Implement the TicTacToe class:

    TicTacToe(int n) Initializes the object the size of the board n.
    int move(int row, int col, int player) Indicates that player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move.

Follow up:
Could you do better than O(n2) per move() operation?

Example 1:

Input
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
Output
[null, 0, 0, 0, 0, 0, 0, 1]

Explanation
TicTacToe ticTacToe = new TicTacToe(3);
Assume that player 1 is "X" and player 2 is "O" in the board.
ticTacToe.move(0, 0, 1); // return 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

ticTacToe.move(0, 2, 2); // return 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

ticTacToe.move(2, 2, 1); // return 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

ticTacToe.move(1, 1, 2); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

ticTacToe.move(2, 0, 1); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

ticTacToe.move(1, 0, 2); // return 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|

Constraints:

    2 <= n <= 100
    player is 1 or 2.
    1 <= row, col <= n
    (row, col) are unique for each different call to move.
    At most n2 calls will be made to move.

"""


class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board = []
        for _ in range(n):
            array = []
            for _ in range(n):
                array.append(0)
            self.board.append(array)

        self.right_diagonal = set()
        self.left_diagonal = set()
        self.left_diagonal_value = []
        self.right_diagonal_value = []
        for row in range(n):
            self.right_diagonal.add((row, row))

        for row in range(n):
            # for col in range(n-1, -1, -1):
            self.left_diagonal.add((row, n-1-row))

        #print(self.right_diagonal)
        #print(self.left_diagonal)

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        # check_right_diagonal = False
        # check_left_diagonal = False
        # check_vertical = False
        # check_horizontal = False

        # check right diagonal
        self.board[row][col] = player

        if (row, col) in self.right_diagonal:
            self.right_diagonal_value.append(player)
            #print(row, col)
            if len(self.right_diagonal_value) == len(self.board) and \
                sum(self.right_diagonal_value) == len(self.board) * player:

                return player
        # check left diagonal
        if (row, col) in self.left_diagonal:
            self.left_diagonal_value.append(player)
            if len(self.left_diagonal_value) == len(self.board) and \
                sum(self.left_diagonal_value) == len(self.board) * player:
                return player
        
        # check vertical
        for i in range(len(self.board)):
            if self.board[i][col] != player:
                break

        else:

            return player


        # check horizontal

        for j in range(len(self.board)):

            if self.board[row][j] != player:
                break
        
        else:
            return player

        #print(self.board, self.right_diagonal_value, self.left_diagonal_value)
        return 0

# Your TicTacToe object will be instantiated and called as such:


obj = TicTacToe(2)
print(obj.move(0,0,2))
print(obj.move(0,1,1))
print(obj.move(1,1,2))
