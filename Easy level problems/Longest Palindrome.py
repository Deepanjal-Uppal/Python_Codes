# PROBLEM:

# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

# SOLUTION:

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        d = Counter(s)
        c = 0
        odd = 1
        
        for i in d:
            if d[i] % 2 == 0:
                c += d[i]
            else:
                if d[i] == 1 and odd > 0:
                    c += d[i]
                    odd -= 1
                elif odd > 0:
                    c += d[i]
                    odd -= 1
                else:
                    c += (d[i] -1)
        
        return c
