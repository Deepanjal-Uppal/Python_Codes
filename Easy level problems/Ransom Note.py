# PROBLEM:

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example:

# Input: ransomNote = "a", magazine = "b"
# Output: false

# SOLUTION:

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        m = Counter(magazine)
        li = [x for x in ransomNote]

        for i in range(len(ransomNote)):
            if ransomNote[i] in m:
                if m[ransomNote[i]] > 0:
                    m[ransomNote[i]] -= 1
                    li.remove(ransomNote[i])
                else:
                    return False

        
        if len(li) == 0:
            return True
        else:
            return False
