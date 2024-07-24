# PROBLEM:

# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.

# Example:

# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3

# SOLUTION:

class Solution:
    def isUgly(self, n: int) -> bool:

        while n > 1:
            if n % 5 == 0:
                n = n // 5
            elif n % 3 == 0:
                n = n // 3
            elif n % 2 == 0:
                n = n //2
            else:
                break
        
        return n == 1
