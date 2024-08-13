# PROBLEM:

# You are a hiker preparing for an upcoming hike. 
# You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). 
# You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). 
# You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

# Example:

# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

# SOLUTION:

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        minHeap = [[0, 0, 0]] # diff, row, col
        visited = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r == ROWS - 1 and c == COLS - 1:
                return diff
            
            for dr, dc in directions:
                newR, newC = dr + r, dc + c
                if newR < 0 or newC < 0 or newR == ROWS or newC == COLS or (newR, newC) in visited:
                    continue
                newDiff = max(diff, abs(heights[r][c] - heights[newR][newC]))
                heapq.heappush(minHeap, [newDiff, newR, newC])
