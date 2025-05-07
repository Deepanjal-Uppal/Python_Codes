# PROBLEM:

# There is a dungeon with n x m rooms arranged as a grid.
# You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. 
# Moving between adjacent rooms takes exactly one second.
# Return the minimum time to reach the room (n - 1, m - 1).
# Two rooms are adjacent if they share a common wall, either horizontally or vertically.

# Example:
# Input: moveTime = [[0,4],[4,4]]
# Output: 6
# Explanation:
# The minimum time required is 6 seconds.
# At time t == 4, move from room (0, 0) to room (1, 0) in one second.
# At time t == 5, move from room (1, 0) to room (1, 1) in one second.

# SOLUTION:

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        ROWS, COLS = len(moveTime) - 1, len(moveTime[0]) - 1
        min_heap = [(0, 0, 0)]
        visited = set()

        while min_heap:
            cur_sec, cur_r, cur_c = heappop(min_heap)
            if (cur_r, cur_c) in visited:
                continue
            if cur_r == ROWS and cur_c == COLS:
                return cur_sec
            moveTime[cur_r][cur_c] = cur_sec
            visited.add((cur_r, cur_c))
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = cur_r + x, cur_c + y
                if 0 <= new_r <= ROWS and 0 <= new_c <= COLS:
                    heappush(min_heap, (max(cur_sec + 1, moveTime[new_r][new_c] + 1), new_r, new_c))
