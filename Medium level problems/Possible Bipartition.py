# PROBLEM:

# We want to split a group of n people (labeled from 1 to n) into two groups of any size. 
# Each person may dislike some other people, and they should not go into the same group.

# Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, 
# return true if it is possible to split everyone into two groups in this way.

# Example:

# Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: The first group has [1,4], and the second group has [2,3].

# SOLUTION:

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for u, v in dislikes:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)

        color = [-1] * n
        def dfs(node, col):
            color[node] = col
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    if not dfs(neighbor, not col):
                        return False
                elif color[neighbor] == col:
                    return False
            return True
        for i in range(n):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        return True
