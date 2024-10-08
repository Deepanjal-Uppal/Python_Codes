# PROBLEM:

# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
# That means the first house is the neighbor of the last one. 
# Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police 
# if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting the police. 

# Example:

# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

# SOLUTION:

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(start, end):
            rob1, rob2 = 0, 0

            for i in range(start, end):
                temp = max(rob1 + nums[i], rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        first = helper(0, len(nums) - 1)  
        second = helper(1, len(nums))
        return max(first, second) 
