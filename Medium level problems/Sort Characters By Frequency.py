# PROBLEM:

# Given a string s, sort it in decreasing order based on the frequency of the characters. 
# The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

# Example:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

# SOLUTION:

class Solution:
    def frequencySort(self, s: str) -> str:
        
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        h = []
        for i in d:
            h.append((-d[i], i))
        
        res = ""
        heapq.heapify(h)
        while len(h):
            freq, ele = heapq.heappop(h)
            res += ele * abs(freq)

        return res
