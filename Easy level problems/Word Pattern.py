# PROBLEM:

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

# Example:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

# SOLUTION:

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        li = s.split()
        maptos, mapsto = {}, {}

        if len(li) != len(pattern):
            return False

        for i in range(len(li)):
            if ((pattern[i] in maptos and maptos[pattern[i]] != li[i]) or 
            (li[i] in mapsto and mapsto[li[i]] != pattern[i])) :
                return False
            else:
                maptos[pattern[i]] = li[i]
                mapsto[li[i]] = pattern[i]

        return True
