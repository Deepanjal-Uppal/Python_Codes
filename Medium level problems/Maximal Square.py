# PROBLEM:

# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Example:

# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4

# SOLUTION:

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}

        def helper(r, c):
            if r >= ROWS or c >= COLS:
                return 0

            if (r, c) not in cache:
                right = helper(r + 1, c)
                down = helper(r, c + 1)
                diag = helper(r + 1, c + 1)

                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(right, down, diag)

            return cache[(r,c)]

        helper(0, 0)
        return max(cache.values()) ** 2   #for returning area multiply by 2
