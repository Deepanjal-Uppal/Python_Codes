# PROBLEM:

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# SOLUTION:

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        s = list(set(nums))
        s.sort()
        print(s)
        res = 1
        l = 1

        for i in range(1, len(s)):
            if s[i] - s[i - 1] == 1:
                l += 1
            else:
                l = 1
            res = max(res, l)

        return res
