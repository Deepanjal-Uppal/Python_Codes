# PROBLEM:

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# SOLUTION:

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        if len(strs) == 1:
            return strs[0]

        for i in range(len(strs[0])):
            c = 1
            curr = strs[0][i]
            for j in range(1, len(strs)):
                if len(strs[j]) <= i:
                    return res
                if strs[j][i] == curr:
                    c += 1
                else:
                    return res
                if c == len(strs):
                    res += curr
                    
        return res
