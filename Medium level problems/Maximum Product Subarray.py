# PROBLEM:

# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.

# Example:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# SOLUTION:

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        mini, maxi = 1, 1

        for i in nums:
            temp = maxi * i
            maxi = max(maxi * i, mini * i, i)
            mini = min(temp, mini * i, i)
            res = max(res, maxi)

        return res
