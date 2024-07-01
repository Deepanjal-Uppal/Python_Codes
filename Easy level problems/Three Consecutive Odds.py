# PROBLEM:

# Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 
# Example:

# Input: arr = [2,6,4,1]
# Output: false
# Explanation: There are no three consecutive odds.

# SOLUTION:

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd = 0

        for i in arr:
            if i % 2 != 0:
                odd += 1
            else:
                odd = 0
            if odd == 3:
                return True

        return False
