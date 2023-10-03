# PROBLEM:

# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Example:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# SOLUTION:

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        d = {i : nums.count(i) for i in set(nums)}
        s = 0

        for i in d:
            s += (d[i] * (d[i] - 1) // 2)

        return s
        
