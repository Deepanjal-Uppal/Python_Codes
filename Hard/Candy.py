# PROBLEM:

# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

# Example:

# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

# SOLUTION:

class Solution:
    def candy(self, ratings: List[int]) -> int:

        st = [1] * len(ratings)

        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i - 1]:
                st[i] = st[i-1] + 1
        
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1] and st[i] <= st[i + 1]:
                    st[i] = st[i + 1] + 1
    

        return sum(st)
