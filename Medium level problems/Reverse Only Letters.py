# PROBLEM:

# Given a string s, reverse the string according to the following rules:

# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

# Example:

# Input: s = "ab-cd"
# Output: "dc-ba"

# SOLUTION:

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l].isalpha() and s[r].isalpha():
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif not s[l].isalpha() and s[r].isalpha():
                l += 1
            elif s[l].isalpha() and not s[r].isalpha():
                r -= 1
            else:
                l += 1
                r -= 1
        return ''.join(s)
