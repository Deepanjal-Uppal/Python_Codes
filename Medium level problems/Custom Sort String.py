# PROBLEM:

# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, 
# then x should occur before y in the permuted string.

# Return any permutation of s that satisfies this property.

# Example:

# Input:  order = "cba", s = "abcd" 
# Output:  "cbad" 
# Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
# Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

# SOLUTION:

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {}

        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        res = ""
        for i in order:
            if i in s:
                while d[i] > 0:
                    res += i
                    d[i] -= 1
                if d[i] == 0:
                    del d[i]
        
        for i in d:
            while d[i] > 0:
                res += i
                d[i] -= 1
        return res
