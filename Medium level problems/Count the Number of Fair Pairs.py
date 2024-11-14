# PROBLEM:

# Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

# A pair (i, j) is fair if:
#   0 <= i < j < n, and
#   lower <= nums[i] + nums[j] <= upper
 
# Example:

# Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
# Output: 6
# Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

# SOLUTION:

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        def countpairs(target):
            i, j = 0, len(nums) - 1
            res = 0
            while i < j:
                if nums[i] + nums[j] <= target:
                    res += (j - i)
                    i += 1
                else:
                    j -= 1
            return res
        totalupper = countpairs(upper)
        totallower = countpairs(lower - 1)
        return totalupper - totallower
