# PROBLEM:

# You are given an integer array nums.

# In one move, you can choose one element of nums and change it to any value.

# Return the minimum difference between the largest and smallest value of nums after performing at most three moves.

# Example:

# Input: nums = [5,3,2,4]
# Output: 0
# Explanation: We can make at most 3 moves.
# In the first move, change 2 to 3. nums becomes [5,3,3,4].
# In the second move, change 4 to 3. nums becomes [5,3,3,3].
# In the third move, change 5 to 3. nums becomes [3,3,3,3].
# After performing 3 moves, the difference between the minimum and maximum is 3 - 3 = 0.

# SOLUTION:

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
        start = 0
        end = len(nums) - 3 - 1
        diff = nums[-1] - nums[0]
        res = diff

        while end < len(nums):
            diff = nums[end] - nums[start]
            res = min(res, diff)
            start += 1
            end += 1

        return res
