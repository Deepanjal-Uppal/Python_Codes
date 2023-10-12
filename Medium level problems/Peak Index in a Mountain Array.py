# PROBLEM:

# An array arr is a mountain if the following properties hold:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# 1. arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# 2. arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

# You must solve it in O(log(arr.length)) time complexity.

# Example:

# Input: arr = [0,1,0]
# Output: 1

# SOLUTION:

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        l = 1 
        r = len(arr) - 2

        while l <= r:
            m = (l + r) // 2
            if arr[m - 1] < arr[m] > arr[m + 1]:
                return m 
            elif arr[m - 1] < arr[m] < arr[m + 1]:
                l = m + 1
            else:
                r = m - 1
