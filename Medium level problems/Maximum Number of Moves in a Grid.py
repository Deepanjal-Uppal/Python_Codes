# PROBLEM:

# You are given a 0-indexed m x n matrix grid consisting of positive integers.

# You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

# From a cell (row, col), you can move to any of the cells: 
# (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) 
# such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
# Return the maximum number of moves that you can perform.

# Example:

# Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
# Output: 3
# Explanation: We can start at the cell (0, 0) and make the following moves:
# - (0, 0) -> (0, 1).
# - (0, 1) -> (1, 2).
# - (1, 2) -> (2, 3).
# It can be shown that it is the maximum number of moves that can be made.

# SOLUTION:

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dp = [[0] * COLS for _ in range(ROWS)]
        res = 0

        for c in range(COLS - 2, -1, -1):
            for r in range(ROWS):
                if r > 0 and grid[r][c] < grid[r - 1][c + 1]:
                    dp[r][c] = max(dp[r][c], dp[r - 1][c + 1] + 1)
                if grid[r][c] < grid[r][c + 1]:
                    dp[r][c] = max(dp[r][c], dp[r][c + 1] + 1)
                if r < ROWS - 1 and grid[r][c] < grid[r + 1][c + 1]:
                    dp[r][c] = max(dp[r][c], dp[r + 1][c + 1] + 1)

        for r in range(ROWS):
            res = max(res, dp[r][0])
        return res

        return 
