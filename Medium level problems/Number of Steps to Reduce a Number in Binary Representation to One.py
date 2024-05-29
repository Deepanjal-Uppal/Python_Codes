# PROBLEM:

# Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

# If the current number is even, you have to divide it by 2.

# If the current number is odd, you have to add 1 to it.

# It is guaranteed that you can always reach one for all test cases.

# Example:

# Input: s = "1101"
# Output: 6
# Explanation: "1101" corressponds to number 13 in their decimal representation.
# Step 1) 13 is odd, add 1 and obtain 14. 
# Step 2) 14 is even, divide by 2 and obtain 7.
# Step 3) 7 is odd, add 1 and obtain 8.
# Step 4) 8 is even, divide by 2 and obtain 4.  
# Step 5) 4 is even, divide by 2 and obtain 2. 
# Step 6) 2 is even, divide by 2 and obtain 1.  

# SOLUTION:

class Solution:
    def numSteps(self, s: str) -> int:
        p = len(s) - 1
        num = 0
        for i in s:
            if i == "1":
                n = 2 ** p
                num += n
            p -= 1
        
        steps = 0
        while num != 1:
            if num % 2 != 0:
                num += 1
            else:
                num = num // 2
            steps += 1
            
        return steps
