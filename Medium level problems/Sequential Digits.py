# PROBLEM:

# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

# Example:

# Input: low = 100, high = 300
# Output: [123,234]

# SOLUTION:

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        res = []

        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if low <= int(s[i : j + 1]) <= high:
                    res.append(int(s[i : j + 1]))

        res.sort()
        return res
