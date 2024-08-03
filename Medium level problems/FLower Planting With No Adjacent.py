# PROBLEM:

# You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [xi, yi] describes a bidirectional path between garden xi to garden yi. 
# In each garden, you want to plant one of 4 types of flowers.

# All gardens have at most 3 paths coming into or leaving it.

# Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

# Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)th garden. 
# The flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists.

# Example:

# Input: n = 3, paths = [[1,2],[2,3],[3,1]]
# Output: [1,2,3]
# Explanation:
# Gardens 1 and 2 have different types.
# Gardens 2 and 3 have different types.
# Gardens 3 and 1 have different types.
# Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2], and [3,2,1].

SOLUTION:

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        d = defaultdict(set)

        for u, v in paths:
            d[u].add(v)
            d[v].add(u)

        availableColor = defaultdict(set)
        for i in range(1, n + 1):
            availableColor[i] = {1, 2, 3, 4}

        res = []

        for i in range(1, n + 1):
            color = availableColor[i].pop()
            res.append(color)
            for j in d[i]:
                if color in availableColor[j]:
                    availableColor[j].remove(color)

        return res
