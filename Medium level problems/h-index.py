# PROBLEM:

# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least 
# h papers that have each been cited at least h times.

# Example:

# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

# SOLUTION:

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        arr = [0] * (len(citations) + 1)
        for i in citations:
            if i > len(citations):
                arr[-1] += 1
            else:
                arr[i] += 1
        
        c = 0
        for i in range(len(arr) - 1, -1, -1):
            c += arr[i]
            if c >= i:
                return i
            
