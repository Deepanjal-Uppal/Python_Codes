# PROBLEM:

# You are given a 0-indexed string s and a dictionary of words dictionary. 
# You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. 
# There may be some extra characters in s which are not present in any of the substrings.

# Return the minimum number of extra characters left over if you break up s optimally.

# Example:

# Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
# Output: 1
# Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

# SOLUTION:

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        dp = {len(s) : 0}

        def dfs(i):
            if i in dp:
                return dp[i]

            res = 1 + dfs(i + 1)
            for j in range(i, len(s)):
                if s[i : j + 1] in words:
                    res = min(res, dfs(j + 1))
            dp[i] = res
            return res

        return dfs(0)
