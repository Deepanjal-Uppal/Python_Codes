# PROBLEM:

# You are given an integer num. You can swap two digits at most once to get the maximum valued number.

# Return the maximum valued number you can get.

# Example:

# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.

# SOLUTION:

class Solution:
    def maximumSwap(self, num: int) -> int:
        li = list(str(num))
        length = len(li)

        for i in range(length):
            if i + 1 < length and li[i] < max(li[i + 1:]):
                m = max(li[i + 1:])
                idx = len(li) - 1 - li[::-1].index(m)
                li[i], li[idx] = li[idx],li[i]
                break
        
        return int(''.join(li))
