# PROBLEM:

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# SOLUTION:

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x : x[0])
        i = 1
        while i < len(intervals):
            start1, end1 = intervals[i - 1]
            start2, end2 = intervals[i]

            if start2 <= end1 and end1 <= end2:
                intervals[i - 1][1] = end2
                intervals.pop(i)
            elif start2 <= end1 and end1 >= end2:
                intervals.pop(i)
            else:
                i += 1

        return intervals
