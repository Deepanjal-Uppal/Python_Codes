# PROBLEM:

# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval 
# and intervals is sorted in ascending order by starti. 
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti 
# and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.

# Example:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# SOLUTION:

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)

        intervals.sort(key = lambda x : x[0])
        i = 1
        while i < len(intervals):
            start1, end1 = intervals[i - 1]
            start2, end2 = intervals[i]

            if start2 <= end1 and end1 <= end2:
                intervals.pop(i)
                intervals[i - 1][1] = end2

            elif start2 <= end1 and end1 >= end2:
                intervals.pop(i)
            else:
                i += 1
                
        return intervals 
