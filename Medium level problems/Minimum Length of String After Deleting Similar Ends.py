# PROBLEM:

# Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

# Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
# Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
# The prefix and the suffix should not intersect at any index.
# The characters from the prefix and suffix must be the same.
# Delete both the prefix and the suffix.
# Return the minimum length of s after performing the above operation any number of times (possibly zero times).

# Example:

# Input: s = "ca"
# Output: 2

# SOLUTION:

class Solution:
    def minimumLength(self, s: str) -> int:
        start = 0
        end = len(s) - 1

        while start < end :
            if s[start] == s[end]:
                start += 1
                end -= 1
            elif start != 0 and s[start] == s[start - 1]:
                start += 1
            elif end != len(s) - 1 and s[end] == s[end + 1]:
                end -= 1
            else:
                print(s[start : end + 1])
                return len(s[start : end + 1])
                
        if len(s[start : end + 1]) == 1 and start != 0 and s[start] == s[start - 1]:
                start += 1

        return len(s[start : end + 1])
