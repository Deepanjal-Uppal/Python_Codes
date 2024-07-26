# PROBLEM:

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 
# Example:

# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# SOLUTION:

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subbox = [set() for _ in range(len(board) // 3)]
        
        for r in range(len(board)):
            rows = set()
            cols = set()

            if r % 3 == 0:
                subbox = [set() for _ in range(len(board) // 3)]

            for c in range(len(board[0])):
                if board[r][c] != ".":
                    if board[r][c] in rows or board[r][c] in subbox[c // 3]:
                        return False
                    rows.add(board[r][c])
                    subbox[c // 3].add(board[r][c])

                if board[c][r] != ".":
                    if board[c][r] in cols:
                        return False
                    cols.add(board[c][r])
                    
        return True
