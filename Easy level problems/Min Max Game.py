# PROBLEM:

# You are given a 0-indexed integer array nums whose length is a power of 2.

# Apply the following algorithm on nums:

# Let n be the length of nums. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n / 2.
# For every even index i where 0 <= i < n / 2, assign the value of newNums[i] as min(nums[2 * i], nums[2 * i + 1]).
# For every odd index i where 0 <= i < n / 2, assign the value of newNums[i] as max(nums[2 * i], nums[2 * i + 1]).
# Replace the array nums with newNums.
# Repeat the entire process starting from step 1.
# Return the last number that remains in nums after applying the algorithm.

# Example:

# Input: nums = [1,3,5,2,4,8,2,2]
# Output: 1
# Explanation: The following arrays are the results of applying the algorithm repeatedly.
# First: nums = [1,5,4,2]
# Second: nums = [1,4]
# Third: nums = [1]
# 1 is the last remaining number, so we return 1.

# SOLUTION:

if len(nums) == 1:
            return nums[0]

        while len(nums) != 1:
            res = []
            for i in range(0, len(nums)//2):
                if i % 2 == 0:
                    res.append(min(nums[2 * i], nums[(2 * i) + 1]))
                else:
                    res.append(max(nums[2 * i], nums[(2 * i) + 1]))

            nums = res

        return nums[0]
