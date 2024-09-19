# PROBLEM:

# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. 
# It is guaranteed there is at least one word that is not banned, and that the answer is unique.

# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

# Example:

# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banned.

# SOLUTION:

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        def helper(s):
            new_s = ""
            for i in s:
                if i.isalpha():
                    new_s += i
                    
            return new_s

        temp = paragraph.lower().replace(',', ' ').split(' ')
        li = [word for word in temp if word != '']
        d = defaultdict(int)

        for s in li:
            if s.isalpha() == True:
                if s not in banned:
                    d[s] += 1
            else:
                s = helper(s)
                if s not in banned:
                    d[s] += 1
        
        Keymax = max(zip(d.values(), d.keys()))[1]
        return Keymax
