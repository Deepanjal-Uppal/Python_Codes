# PROBLEM:

# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), 
# return the next greater number for every element in nums.
 
# The next greater number of a number x is the first greater number to its traversing-order next in the array, 
# which means you could search circularly to find its next greater number. 
# If it doesn't exist, return -1 for this number.

# Example:

# Input: nums = [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; 
# The number 2 can't find next greater number. 
# The second 1's next greater number needs to search circularly, which is also 2.

# SOLUTION:

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        m = max(nums)
        st = []

        for i in range(len(nums)):
            if nums[i] == m:
                st.append(-1)
            else:
                for j in range(i+1, len(nums)):
                    if nums[j] > nums[i]:
                        st.append(nums[j])
                        break
                else:
                    for j in range(0, i):
                        if nums[j] > nums[i]:
                            st.append(nums[j])
                            break
        return st
