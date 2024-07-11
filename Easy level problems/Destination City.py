# PROBLEM:

# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. 
# Return the destination city, that is, the city without any path outgoing to another city.

# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

 

# Example 1:

# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo" 
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> 
#              "Lima" -> "Sao Paulo".

# SOLUTION:

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}

        for city1, city2 in paths:
            if city1 not in d:
                d[city1] = []
            if city2 not in d:
                d[city2] = []
            d[city1].append(city2)
        
        for i in d:
            if len(d[i]) == 0:
                return i

        
