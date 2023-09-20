PROBLEM:

Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example:

Input: x = -123
Output: -321

SOLUTION:

class Solution:
    def reverse(self, x: int) -> int:

        s = str(x)
        rev = s[::-1]
        res = 0
        c = 0

        for i in rev:
            if i == 0 and c == 0:
                res = 0
            elif i == "-":
                res *= (-1)
            else:
                res = res * 10
                res += int(i)
                c += 1
        
        if res > 2**31 or res < (-2)**31:
            return 0

        return res
