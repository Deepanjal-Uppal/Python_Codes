# PROBLEM:

# You are given an integer array nums. A subsequence of nums is called a square streak if:

# The length of the subsequence is at least 2, and
# after sorting the subsequence, each element (except the first element) is the square of the previous number.
# Return the length of the longest square streak in nums, or return -1 if there is no square streak.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

# Example:

# Input: nums = [4,3,6,16,8,2]
# Output: 3
# Explanation: Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].
# - 4 = 2 * 2.
# - 16 = 4 * 4.
# Therefore, [4,16,2] is a square streak.
# It can be shown that every subsequence of length 4 is not a square streak.

# SOLUTION:

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        h = defaultdict(int)

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] ** 2 in h:
                h[nums[i]] = h[nums[i] ** 2] + 1
            else:
                h[nums[i]] = 1
        
        res = max(h.values())

        return res if res != 1 else -1
