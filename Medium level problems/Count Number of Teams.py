# PROBLEM:

# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

# You have to form a team of 3 soldiers amongst them under the following rules:

# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

# Example:

# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

# SOLUTION:

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0

        for m in range(1, len(rating) - 1):
            left_smaller = right_larger = 0
            for i in range(0, m):
                if rating[i] < rating[m]:
                    left_smaller += 1
            for j in range(m + 1, len(rating)):
                if rating[j] > rating[m]:
                    right_larger += 1
            res += (left_smaller * right_larger)
            left_larger = m - left_smaller
            right_smaller = len(rating) - m - 1 - right_larger
            res += (left_larger * right_smaller)

        return res
