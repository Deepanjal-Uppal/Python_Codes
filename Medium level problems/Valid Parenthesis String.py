# PROBLEM:

# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

# The following rules define a valid string:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

# Example:

# Input: s = "()"
# Output: true

# SOLUTION:

class Solution:
    def checkValidString(self, s: str) -> bool:
        
        leftmin, leftmax = 0, 0

        for c in s:
            if c == "(":
                leftmin, leftmax = leftmin + 1, leftmax + 1
            elif c == ")":
                leftmin, leftmax = leftmin - 1, leftmax - 1
            else:
                leftmin, leftmax = leftmin - 1, leftmax + 1
            if leftmax < 0:
                return False
            if leftmin < 0:
                leftmin = 0 # s = (*)(
        return leftmin == 0
