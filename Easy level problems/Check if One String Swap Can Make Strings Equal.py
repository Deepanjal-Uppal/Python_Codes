# PROBLEM:

# You are given two strings s1 and s2 of equal length. 
# A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. 
# Otherwise, return false.

# Example:

# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap the first character with the last character of s2 to make "bank".

# SOLUTION:

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        s1 = list(s1)
        s2 = list(s2)
        
        pos1 = pos2 = -1
        i = 0
        while i < len(s1):
            if s1[i] != s2[i]:
                if pos1 == -1:
                    pos1 = i
                else:
                    pos2 = i
                    s2[pos1], s2[pos2] = s2[pos2], s2[pos1]
                    break
            i += 1
     
        if s1 == s2:
            return True
        return False
