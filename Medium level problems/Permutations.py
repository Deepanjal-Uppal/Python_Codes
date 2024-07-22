# PROBLEM:

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# SOLUTION:

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
            else:
                for i in range(len(nums)):
                    if nums[i] not in path:
                        dfs(path + [nums[i]])
        
        res = []
        dfs([])
        return res
