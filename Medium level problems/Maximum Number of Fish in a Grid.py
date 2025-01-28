# PROBLEM:

# You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

# A land cell if grid[r][c] = 0, or
# A water cell containing grid[r][c] fish, if grid[r][c] > 0.
# A fisher can start at any water cell (r, c) and can do the following operations any number of times:

# Catch all the fish at cell (r, c), or
# Move to any adjacent water cell.
# Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

# An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

# Example:

# Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
# Output: 7
# Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.

# SOLUTION:

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[0] * COLS for _ in range(ROWS)]
        
        def dfs(r, c):
            nonlocal cnt
            cnt += grid[r][c]
            visited[r][c] = 1
            neighbor = [[r, c + 1], [r, c - 1], [r + 1, c], [r - 1, c]]
            for nr, nc in neighbor:
                if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 0 or visited[nr][nc] == 1:
                    continue
                dfs(nr, nc)
                visited[nr][nc] = 1
            return cnt

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] > 0 and visited[r][c] == 0:
                    cnt = 0
                    val = dfs(r, c)
                    res = max(res, val)  
                else:
                    visited[r][c] = 1     
        return res
