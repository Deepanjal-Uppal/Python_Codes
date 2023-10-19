# PROBLEM:

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

# Example:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

# SOLUTION:

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        l1=[]
        l2=[]

        for i in s[:]:
            if  i =="#":
                if len(l1)>0:
                    l1.pop()
            else:
                l1.append(i)

        for i in t[:]:
            if  i =="#":
                if len(l2)>0:
                    l2.pop()
            else:
                l2.append(i)
        
        if l1==l2:
            return True 
        else:
            return False
