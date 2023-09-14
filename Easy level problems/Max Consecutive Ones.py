# PROBLEM:

# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# SOLUTION:

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        c = 0
        res = 0

        for i in nums:
            if i == 1:
                c += 1
            else:
                c = 0
            res = max(c,res)

        return res        
