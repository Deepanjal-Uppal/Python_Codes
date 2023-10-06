# PROBLEM:

# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

# Return the maximum product you can get.

# Example:

# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.

# SOLUTION:

class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp = { 1 : 1 }

        def dfs(num):
            if num in dp:
                return dp[num]
            
            dp[num] = 0 if num == n else num
            for i in range(1,num):
                val = dfs(i) * dfs(num - i)
                dp[num] = max(dp[num], val)
            return dp[num]

        return dfs(n)
