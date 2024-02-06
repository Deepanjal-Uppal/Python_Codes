# PROBLEM:

# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

# Example:

# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

# SOLUTION:

class Solution:
    def tribonacci(self, n: int) -> int:

        F = [0, 1, 1]
        if n == 0:
            return F[0]
        elif n == 1:
            return F[1]
        elif n == 2:
            return F[2]
        
        for i in range(3, n + 1):
            F.append(F[i - 1] + F[i - 2] + F[i - 3])

        return F[n]
