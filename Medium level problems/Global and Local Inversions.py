# PROBLEM:

# You are given an integer array nums of length n which represents a permutation of all the integers in the range [0, n - 1].

# The number of global inversions is the number of the different pairs (i, j) where:
# 1) 0 <= i < j < n
# 2) nums[i] > nums[j]
# The number of local inversions is the number of indices i where:

# 0 <= i < n - 1
# nums[i] > nums[i + 1]
# Return true if the number of global inversions is equal to the number of local inversions.

# Example:

# Input: nums = [1,0,2]
# Output: true
# Explanation: There is 1 global inversion and 1 local inversion.

# SOLUTION:

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        global_inversion = 0
        local_inversion = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                local_inversion += 1
            if i < nums[i]:
                global_inversion += ((nums[i] - i)*(nums[i] - i + 1))//2
        
        return global_inversion == local_inversion
