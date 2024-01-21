# PROBLEM:

# There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. 
# You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. 
# More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

# There are no self-edges (graph[u] does not contain u).
# There are no parallel edges (graph[u] does not contain duplicate values).
# If v is in graph[u], then u is in graph[v] (the graph is undirected).
# The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A
# and a node in set B.

# Return true if and only if it is bipartite.

# Example:

# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

# SOLUTION:

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0 for i in range(len(graph))]
        color = [0 for i in range(len(graph))]

        def bfs(i):
            if visited[i] == 1:
                return True
            visited[i] = 1
            color[i] = -1
            q = deque([i])
            while q:
                i = q.popleft()
                for child in graph[i]:
                    if color[i] == color[child]:
                        return False
                    elif visited[child] == 0:
                        visited[child] = 1
                        color[child] = -1 * color[i]
                        q.append(child)
            return True

        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True
