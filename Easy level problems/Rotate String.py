# PROBLEM:

# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.
 
# Example:

# Input: s = "abcde", goal = "cdeab"
# Output: true

# SOLUTION:

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal):
            return False

        for i in range(len(s)):
            if s[i : ] + s[0 : i] == goal:
                return True
        
        return False
