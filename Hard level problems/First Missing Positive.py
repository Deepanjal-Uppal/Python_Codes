# PROBLEM:

# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

# Example:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.

# SOLUTION:

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        
        for i in range(1, len(nums) + 2):
            if i not in nums:
                return i

        
