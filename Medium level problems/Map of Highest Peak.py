# PROBLEM:

# You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

# If isWater[i][j] == 0, cell (i, j) is a land cell.
# If isWater[i][j] == 1, cell (i, j) is a water cell.
# You must assign each cell a height in a way that follows these rules:

# The height of each cell must be non-negative.
# If the cell is a water cell, its height must be 0.
# Any two adjacent cells must have an absolute height difference of at most 1. 
# A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
# Find an assignment of heights such that the maximum height in the matrix is maximized.

# Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.

# Example:

# Input: isWater = [[0,1],[0,0]]
# Output: [[1,0],[2,1]]
# Explanation: The image shows the assigned heights of each cell.
# The blue cell is the water cell, and the green cells are the land cells.

# SOLUTION:

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(isWater), len(isWater[0])
        visited = set()
        q = deque() #(r, c)
        res = [[-1] * COLS for _ in range(ROWS)]

        #finding all the water cells
        for r in range(ROWS):
            for c in range(COLS):
                if isWater[r][c]:
                    visited.add((r, c))
                    q.append((r, c))
                    res[r][c] = 0

        while q:
            r, c = q.popleft()
            h = res[r][c]

            neighbors = [[r + 1, c], [r, c + 1], [r - 1, c], [r, c - 1]]
            for nr, nc in neighbors:
                if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr, nc) in visited):
                    continue
                q.append((nr, nc))
                visited.add((nr, nc))
                res[nr][nc] = h + 1

        return res
