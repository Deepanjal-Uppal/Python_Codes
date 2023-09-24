# PROBLEM:

# You are given a binary string s that contains at least one '1'.

# You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

# Return a string representing the maximum odd binary number that can be created from the given combination.

# Note that the resulting string can have leading zeros.

# Example:

# Input: s = "010"
# Output: "001"
# Explanation: Because there is just one '1', it must be in the last position. So the answer is "001"

# SOLUTION:

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        if len(s) == 1:
            return s
        b = "010"
        res = ""
        c = 0
        
        for i in s:
            if i == "1":
                c += 1
                
        while c > 1:
            res = res + "1"
            c -= 1
            
        if len(res) + 1 != len(s):  
            while len(res) != len(s) -1:
                res += "0"
                              
        res += "1"
               
        return res
