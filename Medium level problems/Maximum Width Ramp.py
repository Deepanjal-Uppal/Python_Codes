# PROBLEM:

# A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

# Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

# Example:

# Input: nums = [6,0,8,2,1,5]
# Output: 4
# Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.

# SOLUTION:

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        maxi = [0] * len(nums)
        prev = 0
        i = len(nums) - 1

        for n in reversed(nums):
            maxi[i] = max(n, prev)
            prev = maxi[i]
            i -= 1

        res = 0
        r = 1
        
        for l in range(len(nums)):
            while r < len(nums):
                if nums[l] <= maxi[r]:
                    res = max(res, r - l)
                    r += 1
                else:
                    break
        return res
