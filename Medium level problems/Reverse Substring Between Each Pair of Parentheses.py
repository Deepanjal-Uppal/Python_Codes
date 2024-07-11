# PROBLEM:

# You are given a string s that consists of lower case English letters and brackets.

# Reverse the strings in each pair of matching parentheses, starting from the innermost one.

# Your result should not contain any brackets.

# Example:

# Input: s = "(abcd)"
# Output: "dcba"

# SOLUTION:

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for i in s:
            if i == ")":
                portion = []
                while stack[-1] != "(":
                    portion.append(stack.pop())
                stack.pop()
                stack.extend(portion)
            else:
                stack.append(i)

        return "".join(stack)
