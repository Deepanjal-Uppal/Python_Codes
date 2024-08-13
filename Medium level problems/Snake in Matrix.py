# PROBLEM:

# There is a snake in an n x n matrix grid and can move in four possible directions. 
# Each cell in the grid is identified by the position: grid[i][j] = (i * n) + j.

# The snake starts at cell 0 and follows a sequence of commands.

# You are given an integer n representing the size of the grid and an array of strings commands where each command[i] is either "UP", "RIGHT", "DOWN", and "LEFT". 
# It's guaranteed that the snake will remain within the grid boundaries throughout its movement.

# Return the position of the final cell where the snake ends up after executing commands.

# Example:

# Input: n = 2, commands = ["RIGHT","DOWN"]

# Output: 3

# SOLUTION:

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        c = 0
        d={
            "UP": -n,
            "DOWN": n,
            "LEFT": -1,
            "RIGHT": 1
        }
        for i in commands:
            c+=d[i]
        
        return c
