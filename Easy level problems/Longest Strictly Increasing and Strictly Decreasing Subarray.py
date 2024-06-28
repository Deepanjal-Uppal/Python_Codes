# PROBLEM:

# You are given an array of integers nums. Return the length of the longest 
# subarray of nums which is either strictly increasing or strictly decreasing. 

# Example :

# Input: nums = [1,4,3,3,2]

# Output: 2

# Explanation:

# The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].

# The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].

# Hence, we return 2.

# SOLUTION:

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        curr_inc = 1
        curr_dec = 1
        maxi = 1

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                curr_inc += 1
                curr_dec = 1
            elif nums[i] > nums[i + 1]:
                curr_dec += 1
                curr_inc = 1
            else:
                curr_dec = curr_inc = 1

            maxi = max(maxi, curr_inc, curr_dec)

        return maxi
