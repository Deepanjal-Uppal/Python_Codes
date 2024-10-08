# PROBLEM:

# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

# Example:

# Input: grid = [[0,1],[1,0]]
# Output: 2

# SOLUTION:

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque([(0, 0, 1)]) # r, c, length
        visited = set((0, 0))
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]]

        while q:
            r, c, length = q.popleft()
            if (min(r, c) < 0 or max(r, c) >= N or grid[r][c]):
                continue

            if r == N - 1 and c == N - 1:
                return length

            for dr, dc in directions:
                if (dr + r, dc + c) not in visited:
                    q.append((dr + r, dc + c, length + 1))
                    visited.add((r + dr, c + dc))

        return -1
