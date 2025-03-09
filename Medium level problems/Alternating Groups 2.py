# PROBLEM:

# There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

# colors[i] == 0 means that tile i is red.
# colors[i] == 1 means that tile i is blue.
# An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

# Return the number of alternating groups.

# Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

# Example 1:

# Input: colors = [0,1,0,1,0], k = 3

# Output: 3

# SOLUTION:

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        res = 0
        n = len(colors)
        currlen = 1
        prevColor = colors[0]

        for i in range(1, n + k - 1):
            idx = i % n #circular index calculation
            if colors[idx] == prevColor:
                currlen = 1
                prevColor = colors[idx]
                continue
            
            currlen += 1
            if currlen >= k:
                res += 1
            prevColor = colors[idx]
        return res
