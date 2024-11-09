# PROBLEM:

# There is an infinite 2D plane.

# You are given a positive integer k. You are also given a 2D array queries, which contains the following queries:

# queries[i] = [x, y]: Build an obstacle at coordinate (x, y) in the plane. It is guaranteed that there is no obstacle at this coordinate when this query is made.
# After each query, you need to find the distance of the kth nearest obstacle from the origin.

# Return an integer array results where results[i] denotes the kth nearest obstacle after query i, or results[i] == -1 if there are less than k obstacles.

# Note that initially there are no obstacles anywhere.

# The distance of an obstacle at coordinate (x, y) from the origin is given by |x| + |y|.

# Example:

# Input: queries = [[1,2],[3,4],[2,3],[-3,0]], k = 2

# Output: [-1,7,5,3]

# Explanation:

# Initially, there are 0 obstacles.
# After queries[0], there are less than 2 obstacles.
# After queries[1], there are obstacles at distances 3 and 7.
# After queries[2], there are obstacles at distances 3, 5, and 7.
# After queries[3], there are obstacles at distances 3, 3, 5, and 7.

# SOLUTION:

class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        max_heap = []
        res = []

        for x, y in queries:
            val = abs(x) + abs(y)
            if len(max_heap) < k:
                heapq.heappush(max_heap, -val)
            else:
                if abs(max_heap[0]) > val:
                    heapq.heappushpop(max_heap, -val)
            if len(max_heap) == k:
                res.append(-max_heap[0])
            else:
                res.append(-1)
        return res
            

            
