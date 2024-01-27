# PROBLEM:

# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. 
# If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

# Example:

# Input: n = 2, trust = [[1,2]]
# Output: 2

# SOLUTION:

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        adj = {}
        judge = -1
        for i in range(1,n + 1):
            adj[i] = []

        for (u, v) in trust:
            adj[u].append(v)

        for i in adj:
            if len(adj[i]) == 0:
                judge = i

        for i in adj:
            if i != judge and judge not in adj[i]:
                judge = -1
                
        return judge
