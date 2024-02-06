# PROBLEM:

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# SOLUTION:

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for i in strs:
            s = "".join(sorted(i))

            if s not in d:
                d[s] = [i]
            else:
                d[s].append(i)
        
        li = []
        for i in d:
            li.append(d[i])

        return li
