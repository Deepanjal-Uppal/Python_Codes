# PROBLEM:

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that 
# nums[i] == nums[j] and abs(i - j) <= k.

# Example:

# Input: nums = [1,2,3,1], k = 3
# Output: true

# SOLUTION:

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if len(list(set(nums))) == len(nums):
            return False

        for i in range(len(nums)):
            if nums[i] in nums[i + 1 : i + 1 + k]:
                return True

        return False
