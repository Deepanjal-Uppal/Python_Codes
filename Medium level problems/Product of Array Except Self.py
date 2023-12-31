# PROBLEM:

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# OUTPUT:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        p=1

        for i in range(0,len(nums)):
            if nums[i]!=0:
                p*=nums[i]

        c=nums.count(0)

        if c!=len(nums) and c==1:
            for i in range(0,len(nums)):
                if nums[i] == 0:
                    nums[i] = p
                else:
                    nums[i] = 0
        elif c > 1:
            for i in range(0,len(nums)):
                nums[i]=0
        else:
            for i in range(0,len(nums)):
                nums[i]=p//nums[i]

        return nums
