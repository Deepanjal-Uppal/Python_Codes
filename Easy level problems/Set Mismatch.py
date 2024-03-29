# PROBLEM:

# You have a set of integers s, which originally contains all the numbers from 1 to n. 
# Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, 
# which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

# Example:

# Input: nums = [1,2,2,4]
# Output: [2,3]

# SOLUTION:

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1
            
        duplicate, missing = 0, 0

        for i in range(1,len(nums) + 1):
            if i in d:
                if d[i] > 1:
                    duplicate = i
            else:
                missing = i

        return [duplicate, missing]
