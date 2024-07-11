# PROBLEM:

# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

# Return the sum of all the unique elements of nums.

# Example:

# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.

# SOLUTION:

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for i in nums:
            d[i] += 1

        res = 0
        for i in d:
            if d[i] == 1:
                res += i

        return res
