# PROBLEM:

# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, 
# where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

# Example:

# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20

# SOLUTION:

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        adj = {i : [] for i in range(N)}  # i : list of [cost, node] 

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        #prim's algorithms
        visited = set()
        minheap = [[0, 0]]
        res = 0

        while len(visited) < N:
            cost, i = heapq.heappop(minheap)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for neicost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minheap, [neicost, nei])

        return res
