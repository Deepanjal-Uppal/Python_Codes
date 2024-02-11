# PROBLEM:

# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

# Example:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# SOLUTION:

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        def countPalin(l, r, res):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res

        for i in range(len(s)):
            l = r = i
            res = countPalin(i, i, res)
            res = countPalin(i, i + 1, res)
            
        return res
