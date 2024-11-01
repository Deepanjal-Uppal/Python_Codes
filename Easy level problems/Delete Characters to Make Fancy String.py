# PROBLEM:

# A fancy string is a string where no three consecutive characters are equal.

# Given a string s, delete the minimum possible number of characters from s to make it fancy.

# Return the final string after the deletion. It can be shown that the answer will always be unique.

# Example:

# Input: s = "leeetcode"
# Output: "leetcode"
# Explanation:
# Remove an 'e' from the first group of 'e's to create "leetcode".
# No three consecutive characters are equal, so return "leetcode".

# SOLUTION:

class Solution:
    def makeFancyString(self, s: str) -> str:
        res = "" + s[0]
        c = 1
        
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                if c < 2:
                    c += 1
                    res += s[i]
            else:
                c = 1
                res += s[i]
        
        return res
