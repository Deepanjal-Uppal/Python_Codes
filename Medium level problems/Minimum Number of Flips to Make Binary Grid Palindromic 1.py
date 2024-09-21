# PROBLEM:

# You are given an m x n binary matrix grid.

# A row or column is considered palindromic if its values read the same forward and backward.

# You can flip any number of cells in grid from 0 to 1, or from 1 to 0.

# Return the minimum number of cells that need to be flipped to make either all rows palindromic or all columns palindromic.

# Example:

# Input: grid = [[1,0,0],[0,0,0],[0,0,1]]

# Output: 2

# Explanation: Flipping the highlighted cells makes all the rows palindromic.

# SOLUTION:

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        row_operations = 0
        for i in range(ROWS):
            for j in range(COLS // 2):
                if grid[i][j] != grid[i][COLS - j - 1]:
                    row_operations += 1

        col_operations = 0
        for i in range(COLS):
            for j in range(ROWS // 2):
                if grid[j][i] != grid[ROWS - j - 1][i]:
                    col_operations += 1
        return min(row_operations, col_operations)
