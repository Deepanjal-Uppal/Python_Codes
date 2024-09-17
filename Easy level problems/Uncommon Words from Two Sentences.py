# PROBLEM:

# A sentence is a string of single-space separated words where each word consists only of lowercase letters.

# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

# Example:

# Input: s1 = "this apple is sweet", s2 = "this apple is sour"

# Output: ["sweet","sour"]

# Explanation:

# The word "sweet" appears only in s1, while the word "sour" appears only in s2.

# SOLUTION:

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l1 = s1.split()
        l1.extend(s2.split())
        d = defaultdict(int)

        for i in l1:
            d[i] += 1
        
        res = []
        for i in d:
            if d[i] == 1:
                res.append(i)
        return res
