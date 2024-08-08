# PROBLEM:

# You are given a string word containing lowercase English letters.

# Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. 
# For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

# It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. 
# The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. 
# You need to find the minimum number of times the keys will be pushed to type the string word.

# Return the minimum number of pushes needed to type word after remapping the keys.

# An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, '#', and 0 do not map to any letters.

# Example:

# Input: word = "abcde"
# Output: 5
# Explanation: The remapped keypad given in the image provides the minimum cost.
# "a" -> one push on key 2
# "b" -> one push on key 3
# "c" -> one push on key 4
# "d" -> one push on key 5
# "e" -> one push on key 6
# Total cost is 1 + 1 + 1 + 1 + 1 = 5.
# It can be shown that no other mapping can provide a lower cost.

# SOLUTION:

class Solution:
    def minimumPushes(self, word: str) -> int:
        d = defaultdict(int)

        for i in word:
            d[i] += 1
        
        c = 0
        res = 0
        while len(d) > 0:
            c += 1
            ele = max_key = max(d, key=d.get)
            m = d[ele]
            if c <= 8:
                res += m
            elif c > 8 and c <= 16:
                res += (2 * m)
            elif c > 16 and c <= 24:
                res += (3 * m)
            elif c > 24:
                res += (4 * m)
            d.pop(ele)
            
        return res
