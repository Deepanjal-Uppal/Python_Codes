# PROBLEM:

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# SOLUTION:

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums)==0:
            return [-1,-1]

        start = -1
        end = -1
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                start = mid 
                end = mid

                while start - 1 >= 0:
                    if nums[start - 1] != target:
                        break
                    start -= 1
                
                while end + 1 < len(nums):
                    if nums[end + 1] != target:
                        break
                    end += 1
                break

                
            elif nums[mid] > target:
                r = mid - 1

            elif nums[mid] < target:
                l = mid + 1

        return [start, end]
