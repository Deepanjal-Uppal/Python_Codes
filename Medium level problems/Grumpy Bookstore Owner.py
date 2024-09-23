# PROBLEM:

# There is a bookstore owner that has a store open for n minutes. 
# You are given an integer array customers of length n where customers[i] is the number of the customers that enter the store at the start of the ith minute 
# and all those customers leave after the end of that minute.

# During certain minutes, the bookstore owner is grumpy. 
# You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

# When the bookstore owner is grumpy, the customers entering during that minute are not satisfied. Otherwise, they are satisfied.

# The bookstore owner knows a secret technique to remain not grumpy for minutes consecutive minutes, but this technique can only be used once.

# Return the maximum number of customers that can be satisfied throughout the day.

# Example:

# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3

# Output: 16

# Explanation:

# The bookstore owner keeps themselves not grumpy for the last 3 minutes.

# The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

# SOLUTION:

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        i = 0
        j = 0
        unsatisfied = 0
        maxi = 0
        while j < minutes:
            if grumpy[j] == 1:
                unsatisfied += customers[j]
            j += 1
        maxi = unsatisfied

        while j < len(customers):
            if grumpy[i] == 1:
                unsatisfied -= customers[i]
            if grumpy[j] == 1:
                unsatisfied += customers[j]
            i += 1
            j += 1    
            maxi = max(unsatisfied, maxi)

        satisfied = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                satisfied += customers[i]

        return maxi + satisfied
