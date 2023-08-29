# PROBLEM:

# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

# For each index i, names[i] and heights[i] denote the name and height of the ith person.

# Return names sorted in descending order by the people's heights.

# Example:

# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.

# SOLUTION:

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        for i in range(0,len(heights)):
            m = max(heights)
            p = heights.index(m)
            names[i],names[p] = names[p],names[i]
            heights[p] = 0
            heights[i], heights[p] = heights[p], heights[i]
            
        return names
