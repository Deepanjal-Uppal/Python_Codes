(* PROBLEM:

You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. 
Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

Example:

Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

SOLUTION:
 *)
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        row_cnt = [0] * ROWS
        col_cnt = [0] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    row_cnt[r] += 1
                    col_cnt[c] += 1

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (max(row_cnt[r], col_cnt[c]) > 1):
                    res += 1
        return res
