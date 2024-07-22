# PROBLEM:

# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

# Example:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

# SOLUTION:

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        
        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
            else:
                for i in count:
                    if count[i] > 0:
                        count[i] -= 1
                        dfs(path + [i])
                        count[i] += 1

        res = []
        dfs([])
        return res
        
