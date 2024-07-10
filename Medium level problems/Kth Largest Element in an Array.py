# PROBLEM:

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

# Example:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-i for i in nums]
        heapq.heapify(max_heap)

        while k > 0:
            if len(max_heap) > 0:
                res = heapq.heappop(max_heap)
                k -= 1

        return -res
