# PROBLEM:

# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

# Example:

# Input: arr = [2,1]
# Output: false

# SOLUTION:

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        maxi = max(arr)
        index = arr.index(maxi)
        print(index)

        if arr[-1] == maxi or arr[0] == maxi:
            return False

        for i in range(0, index):
            if arr[i] >= arr[i + 1]:
                return False
            
        for j in range(index + 1, len(arr)):
            if arr[j - 1] <= arr[j]:
                return False

        return True
