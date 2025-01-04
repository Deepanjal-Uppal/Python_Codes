# PROBLEM:

# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

# A palindrome is a string that reads the same forwards and backwards.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) 
# deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".

# Example:

# Input: s = "aabca"
# Output: 3
# Explanation: The 3 palindromic subsequences of length 3 are:
# - "aba" (subsequence of "aabca")
# - "aaa" (subsequence of "aabca")
# - "aca" (subsequence of "aabca")

# SOLUTION:

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0

        for ele in set(s):
            i, j = s.find(ele), s.rfind(ele)
            if j > i + 1:
                res += len(set(s[i + 1 : j]))
        return res
