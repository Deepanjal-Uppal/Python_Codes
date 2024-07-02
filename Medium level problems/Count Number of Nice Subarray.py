# PROBLEM:

# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

# Return the number of nice sub-arrays.

# Example:

# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

# SOLUTION:

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        i = 0
        count = 0
        res = 0
        odd = 0

        for j in range(len(nums)):
            if nums[j] % 2 == 1:
                odd += 1
                count = 0
            
            while odd == k:
                if nums[i] % 2 == 1:
                    odd -= 1
                i += 1
                count += 1
            res += count

        return res
