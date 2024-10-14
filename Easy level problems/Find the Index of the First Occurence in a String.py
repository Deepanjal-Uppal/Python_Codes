# PROBLEM:

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# SOLUTION:

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        res = 0

        while i < len(haystack):
            if haystack[i] == needle[j]:
                if j == 0:
                    res = i
                j += 1
                i += 1
                if j == len(needle):
                    return res
            else:
                j = 0
                i = res + 1
                res = i
        return -1
