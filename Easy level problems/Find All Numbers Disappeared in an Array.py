# PROBLEM:

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# Example:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# SOLUTION:

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        li = []

        for i in range(1,len(nums)+1):
            li.append(i)

        return list(set(li) - set(nums))
