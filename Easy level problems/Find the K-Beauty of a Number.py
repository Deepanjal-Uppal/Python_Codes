# PROBLEM:

# The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:
# 1. It has a length of k.
# 2. It is a divisor of num.

# Given integers num and k, return the k-beauty of num.

# Note:
# 1. Leading zeros are allowed.
# 2. 0 is not a divisor of any value.

# A substring is a contiguous sequence of characters in a string.

# Example:

# Input: num = 240, k = 2
# Output: 2
# Explanation: The following are the substrings of num of length k:
# - "24" from "240": 24 is a divisor of 240.
# - "40" from "240": 40 is a divisor of 240.
# Therefore, the k-beauty is 2.

# SOLUTION:

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        s = str(num)
        start = 0
        c = 0
        
        for end in range(k, len(s) + 1):
            if int(s[start : end]) != 0:
                if int(s) % int(s[start : end]) == 0:
                    c += 1
            start += 1

        return c
