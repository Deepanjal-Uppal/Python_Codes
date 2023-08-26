# PROBLEM:

# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

# Example:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# SOLUTION:

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        st = []

        for i in tokens:
            if i is "+":
                a = st.pop()
                b = st.pop()
                c = a + b
                st.append(c)
            elif i is "-":
                a = st.pop()
                b = st.pop()
                c = b - a
                st.append(c)
            elif i is "*":
                a = st.pop()
                b = st.pop()
                c = a * b
                st.append(c)
            elif i is "/":
                a = st.pop()
                b = st.pop()
                c = b / a
                st.append(int(c))
            else:
                st.append(int(i))
        
        return st[0]
