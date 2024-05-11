# PROBLEM:

# There are n workers. 
# You are given two integer arrays quality and wage where quality[i] is the quality of the ith worker and wage[i] is the minimum wage expectation for the ith worker.

# We want to hire exactly k workers to form a paid group. To hire a group of k workers, we must pay them according to the following rules:

# Every worker in the paid group must be paid at least their minimum wage expectation.
# In the group, each worker's pay must be directly proportional to their quality. 
# This means if a worker’s quality is double that of another worker in the group, then they must be paid twice as much as the other worker.
# Given the integer k, return the least amount of money needed to form a paid group satisfying the above conditions. 
# Answers within 10-5 of the actual answer will be accepted.

# Example:

# Input: quality = [10,20,5], wage = [70,50,30], k = 2
# Output: 105.00000
# Explanation: We pay 70 to 0th worker and 35 to 2nd worker.

# SOLUTION:

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        res = float('inf')
        pairs = []

        for i in range(len(quality)):
            pairs.append((wage[i] / quality[i], quality[i]))

        pairs.sort(key = lambda p:p[0])

        maxHeap = []
        total_quality = 0

        for rate, q in pairs:
            heapq.heappush(maxHeap, -q)
            total_quality += q

            if len(maxHeap) > k:
                total_quality += heapq.heappop(maxHeap)

            if len(maxHeap) == k:
                res = min(res, total_quality * rate)

        return res
