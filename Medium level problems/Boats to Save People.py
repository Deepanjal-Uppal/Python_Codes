# PROBLEM:

# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit.
# Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.

# Example:

# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)

# SOLUTION:

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        i, j = 0, len(people) - 1
        
        while i <= j:
            if people[i] + people[j] <= limit and i != j:
                i += 1
                j -= 1
            elif people[j] <= limit:
                j -= 1
            boats += 1
        
        return boats
