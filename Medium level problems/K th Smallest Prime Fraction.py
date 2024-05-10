# PROBLEM:

# You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

# For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

# Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

# Example:

# Input: arr = [1,2,3,5], k = 3
# Output: [2,5]
# Explanation: The fractions to be considered in sorted order are:
# 1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
# The third fraction is 2/5.

# SOLUTION:

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        frac = []

        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                frac.append((arr[i] / arr[j], arr[i] , arr[j]))

        heapq.heapify(frac)
        
        while k:
            val, i, j = heapq.heappop(frac)
            k -= 1

        return [i, j]
