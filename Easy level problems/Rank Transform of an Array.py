# PROBLEM:

# Given an array of integers arr, replace each element with its rank.

# The rank represents how large the element is. The rank has the following rules:

# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.
 
# Example:

# Input: arr = [40,10,20,30]
# Output: [4,1,2,3]
# Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

# SOLUTION:

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(set(arr))
        d = defaultdict()
        res = [0] * len(arr)

        for i, val in enumerate(temp):
            d[val] = i + 1
        
        for i, val in enumerate(arr):
            res[i] = d[val]


        return res      
