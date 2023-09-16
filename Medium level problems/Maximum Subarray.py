# PROBLEM:

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# SOLUTION:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        curr = 0

        for i in nums:
            curr = max(curr + i, i)
            maxi = max(maxi,curr)

        return maxi
        
