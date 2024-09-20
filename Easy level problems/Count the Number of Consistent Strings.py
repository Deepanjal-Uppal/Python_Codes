# PROBLEM:

# You are given a string allowed consisting of distinct characters and an array of strings words. 
# A string is consistent if all characters in the string appear in the string allowed.

# Return the number of consistent strings in the array words.

# Example:

# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

# SOLUTION:

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = 0
        for i in words:
            for j in range(len(i)):
                if i[j] in allowed and j == len(i) - 1:
                    c += 1
                elif i[j] not in allowed:
                    break
        return c
