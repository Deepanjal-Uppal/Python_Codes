# PROBLEM:

# You are given a 0-indexed array nums of integers.

# A triplet of indices (i, j, k) is a mountain if:

# i < j < k
# nums[i] < nums[j] and nums[k] < nums[j]
# Return the minimum possible sum of a mountain triplet of nums. If no such triplet exists, return -1.

# Example:

# Input: nums = [8,6,1,5,3]
# Output: 9
# Explanation: Triplet (2, 3, 4) is a mountain triplet of sum 9 since: 
# - 2 < 3 < 4
# - nums[2] < nums[3] and nums[4] < nums[3]
# And the sum of this triplet is nums[2] + nums[3] + nums[4] = 9. It can be shown that there are no mountain triplets with a sum of less than 9.

# SOLUTION:

class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        
        i, j, k = 0, 1, 2
        res = float('inf')
        s = 0
        
        while k < len(nums):
            while j < len(nums) - 1:
                k = j + 1
                if nums[i] < nums[j] and nums[j] > nums[k]:
                    s = nums[i] + nums[j] + nums[k]
                    res = min(s, res)
            
                if nums[i] < nums[j]:
                    k = j + 1
                    while k < len(nums):
                        if nums[k] < nums[j]:
                            s = nums[i] + nums[j] + nums[k]
                            res = min(s, res)
                        k += 1
                    
                j += 1
            i += 1
            j = i + 1
            k = i + 2
        if res != float('inf'):
            return res
        return -1
