# PROBLEM:

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example:

# Input: s = "leetcode"
# Output: 0

# SOLUTION:

class Solution:
    def firstUniqChar(self, s: str) -> int:

        for i in range(len(s)):
            c = s.count(s[i])
            if c == 1:
                return i
        return -1
            
