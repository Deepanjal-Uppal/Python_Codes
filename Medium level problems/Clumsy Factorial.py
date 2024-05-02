# PROBLEM:

# The factorial of a positive integer n is the product of all positive integers less than or equal to n.

# For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.
# We make a clumsy factorial using the integers in decreasing order by swapping out the multiply operations for a fixed rotation of operations 
# with multiply '*', divide '/', add '+', and subtract '-' in this order.

# For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.
# However, these operations are still applied using the usual order of operations of arithmetic. 
# We do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.

# Additionally, the division that we use is floor division such that 10 * 9 / 8 = 90 / 8 = 11.

# Given an integer n, return the clumsy factorial of n.

# Example:

# Input: n = 4
# Output: 7
# Explanation: 7 = 4 * 3 / 2 + 1

# SOLUTION:

class Solution:
    def clumsy(self, n: int) -> int:
        res = "" + str(n)
        curr_op = 1

        for i in range(n - 1, 0, -1):
            i = str(i)
            if curr_op == 1:
                res += "*" + i
                curr_op += 1
            elif curr_op == 2:
                res += "//" + i
                curr_op += 1
            elif curr_op == 3:
                res += "+" + i
                curr_op += 1
            else:
                res += "-" + i
                curr_op = 1

        res = eval(res)
        return res
