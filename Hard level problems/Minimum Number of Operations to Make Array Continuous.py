# PROBLEM:

# You are given an integer array nums. In one operation, you can replace any element in nums with any integer.

# nums is considered continuous if both of the following conditions are fulfilled:

# All elements in nums are unique.
# The difference between the maximum element and the minimum element in nums equals nums.length - 1.
# For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is not continuous.

# Return the minimum number of operations to make nums continuous.

# Example:

# Input: nums = [4,2,5,3]
# Output: 0
# Explanation: nums is already continuous.

# SOLUTION:

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        length = len(nums)
        nums = sorted(set(nums))
        r = 0
        ans = length

        for l in range(len(nums)):
            while r < len(nums) and nums[r] < nums[l] + length:
                r += 1
            window = r - l
            ans = min(ans, length - window)

        return ans

