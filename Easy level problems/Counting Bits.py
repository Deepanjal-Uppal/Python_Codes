# PROBLEM:

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Example:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# SOLUTION:

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n + 1):
            b =bin(i)
            v = str(b[2:])
            c = 0
            for j in v:
                if j == "1":
                    c += 1
            res.append(c)
            
        return res

        
