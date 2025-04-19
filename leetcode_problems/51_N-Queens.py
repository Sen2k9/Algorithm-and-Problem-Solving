"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:

Input: n = 1
Output: [["Q"]]

 

Constraints:

    1 <= n <= 9


"""
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        col = set()
        posDiag = set()
        negDiag = set()
        board = [["."] * n for _ in range(n)]
        result = []
        def backtrack(r):
            if r == n:
                # the board configuration is maintained by a single string for each row
                copy = ["".join(row) for row in board]
                result.append(copy)
                return

            for c in range(n):
                if c not in col and (r + c) not in posDiag and (r - c) not in negDiag:
                    col.add(c)
                    posDiag.add(r + c)
                    negDiag.add(r - c)
                    board[r][c] = "Q"

                    backtrack(r + 1)

                    col.remove(c)
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)
                    board[r][c] = "."
        backtrack(0)
        return result

if __name__ == '__main__':
    sol = Solution()
    print(
        sol.solveNQueens(3)
    )
    print("\n\n")
    print(
        sol.solveNQueens(4)
    )
    print("\n\n")
    print(
        sol.solveNQueens(5)
    )
    print("\n\n")
    print(
        sol.solveNQueens(1)
    )