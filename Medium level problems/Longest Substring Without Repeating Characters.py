# PROBLEM:

# Given a string s, find the length of the longest substring without repeating characters.

# Example:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# SOLUTION:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        st = []
        m = 1
        l = len(st)

        for i in s:
            if i not in st:
                st.append(i)
            elif i in st:
                j = 0
                while st[j] != i:
                    st.pop(0)
                st.pop(0)
                st.append(i)
            m = max(m,len(st))
        return m
            
        
