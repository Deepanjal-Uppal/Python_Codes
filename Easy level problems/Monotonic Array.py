# PROBLEM:

# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

# Example:

# Input: nums = [1,2,2,3]
# Output: true

# SOLUTION:

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        inc, dec = True, True

        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                inc = False
            elif nums[i-1] < nums[i]:
                dec = False

        return inc or dec
