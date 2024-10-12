# PROBLEM:

# You are given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, 
# that is, multiple frogs can croak at the same time, so multiple "croak" are mixed.

# Return the minimum number of different frogs to finish all the croaks in the given string.

# A valid "croak" means a frog is printing five letters 'c', 'r', 'o', 'a', and 'k' sequentially. 
# The frogs have to print all five letters to finish a croak. If the given string is not a combination of a valid "croak" return -1.

# Example:

# Input: croakOfFrogs = "croakcroak"
# Output: 1 
# Explanation: One frog yelling "croak" twice.

# SOLUTION:

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        d = [0] * 5
        frog = 0
        res = 0
        c ="croak"

        for i in croakOfFrogs:
            index = c.index(i)
            d[index] += 1
            if index > 0 and d[index - 1] < d[index]:
                return -1
            if i == "c":
                frog += 1
            elif i == "k":
                frog -= 1
            res = max(res, frog)

        return res if frog == 0 else -1
