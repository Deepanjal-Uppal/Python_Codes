# PROBLEM:

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Example:

# Input: nums = [3,2,3]
# Output: [3]

# SOLUTION:

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = len(nums) / 3
        li  = []

        for i in set(nums):
            if nums.count(i) > c:
                li.append(i)
        
        return li
        
