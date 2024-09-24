# PROBLEM:

# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

# Example:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

# SOLUTION:

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}

        for i in range(len(s) - 1, -1, -1):
            if s[i] not in last:
                last[s[i]] = i
        print(last)
        i = 0
        j = 0
        res = []

        while j < len(s):
            j = last[s[j]]
            curr = i
            while curr < j:
                up_curr = last[s[curr]]
                j = max(j , up_curr)
                curr += 1
            print(j, s[j])
            j += 1
            res.append(j - i)
            i = j
            
        return res
            
