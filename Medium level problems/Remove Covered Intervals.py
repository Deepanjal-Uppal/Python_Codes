# PROBLEM:

# Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

# The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

# Return the number of remaining intervals.

# Example:

# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

# SOLUTION:

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : (i[0], -i[1]))
        res = [intervals[0]]

        for l, r in intervals[1 : ]:
            prevL, prevR = res[-1]

            if prevL <= l and prevR >= r:
                continue
            res.append([l, r])

        return len(res)

        
