# PROBLEM:

# Given an array of strings nums containing n unique binary strings each of length n, 
# return a binary string of length n that does not appear in nums. 
# If there are multiple answers, you may return any of them.

# Example:

# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.

# SOLUTION:

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        strSet = {s for s in nums}

        def backtrack(i, curr):
            if i == len(nums):
                res = "".join(curr)
                return None if res in strSet else res

            res = backtrack(i + 1, curr)
            if res: return res

            curr[i] = "1"
            res = backtrack(i + 1, curr)
            if res: return res

        
        return backtrack(0, ["0" for s in nums])
