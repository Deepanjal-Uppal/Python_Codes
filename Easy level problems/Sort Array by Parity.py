# PROBLEM:

# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

# Example:

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# SOLUTION:

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        res = []

        for i in nums:
            if i % 2 == 0:
                res.append(i)

        for i in nums:
            if i % 2 != 0:
                res.append(i)

        return res
        
