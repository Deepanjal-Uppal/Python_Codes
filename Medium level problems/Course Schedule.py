# PROBLEM:

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Example:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.

# SOLUTION:

premap = {i : [] for i in range(numCourses)}

        for u,v in prerequisites:
            premap[u].append(v)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if premap[crs] == []:
                return True

            visited.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            premap[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
