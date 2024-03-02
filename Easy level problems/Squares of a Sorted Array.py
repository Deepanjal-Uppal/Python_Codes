# PROBLEM:

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# SOLUTION:

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []

        for i in nums:
            res.append(i * i)

        def merge(nums):
            if len(nums) > 1:
                mid = len(nums) // 2
                left = nums[0 : mid]
                right = nums[mid : ]
                merge(left)
                merge(right)
                i = j = k = 0
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        nums[k] = left[i]
                        i += 1
                    else:
                        nums[k] = right[j]
                        j += 1
                    k += 1

                while i < len(left):
                    nums[k] = left[i]
                    i += 1
                    k += 1

                while j < len(right):
                    nums[k] = right[j]
                    j += 1
                    k += 1
        merge(res)
        return res
