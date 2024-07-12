# PROBLEM:

# You are given a string s and two integers x and y. You can perform two types of operations any number of times.

# Remove substring "ab" and gain x points.
# For example, when removing "ab" from "cabxbae" it becomes "cxbae".
# Remove substring "ba" and gain y points.
# For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# Return the maximum points you can gain after applying the above operations on s.

# Example:

# Input: s = "cdbcbbaaabab", x = 4, y = 5
# Output: 19
# Explanation:
# - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
# - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
# - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
# - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
# Total score = 5 + 4 + 5 + 5 = 19.

# SOLUTION:

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        st_1 = [" "]

        res = 0
        if y > x:
            for i in s:
                if i == "a" and st_1[-1] == "b":
                    res += y
                    st_1.pop()
                else:
                    st_1.append(i)
            st_2 = [" "]
            for i in st_1:
                if i == "b" and st_2[-1] == "a":
                    res += x
                    st_2.pop()
                else:
                    st_2.append(i)
            return res
        else:
            for i in s:
                if i == "b" and st_1[-1] == "a":
                    res += x
                    st_1.pop()
                else:
                    st_1.append(i)
            st_2 = [" "]
            for i in st_1:
                if i == "a" and st_2[-1] == "b":
                    res += y
                    st_2.pop()
                else:
                    st_2.append(i)
            return res
