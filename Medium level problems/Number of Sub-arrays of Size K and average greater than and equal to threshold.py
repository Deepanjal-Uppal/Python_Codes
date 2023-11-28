# PROBLEM:

# Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

# Example:

# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

# SOLUTION:

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        start = 0
        s = sum(arr[0 : k - 1])
        c = 0

        for end in range(k-1, len(arr)):
            s += arr[end]
            if s / k >= threshold:
                c += 1
            s -= arr[start]
            start += 1

        return c
