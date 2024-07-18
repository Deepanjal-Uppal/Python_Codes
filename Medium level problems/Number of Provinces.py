# PROBLEM:

# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, 
# then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

# Example:

# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2

# SOLUTION:

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(i, isConnected, visited):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and not visited[j]:
                    visited[j] = True
                    dfs(j, isConnected, visited)
 
        visited = [False] * len(isConnected)
        res = 0

        for i in range(len(isConnected)):
            if visited[i] == False:
                dfs(i, isConnected, visited)
                res += 1
        return res
