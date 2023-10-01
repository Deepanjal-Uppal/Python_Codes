# PROBLEM:

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Example:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# SOLUTION:

class Solution:
    def reverseWords(self, s: str) -> str:

        rev = []

        for i in s.split():
            rev.append(i[::-1])

        res = "" + rev[0]

        for i in range(1,len(rev)):
            res = res + " " + rev[i]
        
        return res
       
