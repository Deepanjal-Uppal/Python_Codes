# PROBLEM:

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Example:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# SOLUTION:

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        res = 0
        c = 0
        i = 0
        j = 0

        while i < len(nums) and j < len(nums):
            if nums[j] == 1:
                c += 1
                j += 1
            else:
                if k > 0:
                    c += 1
                    k -= 1
                    j += 1
                else:
                    if nums[i] == 0:
                        k += 1
                    i += 1
                    c -= 1
            res = max(res, c)

        return res
