# PROBLEM:

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# SOLUTION:

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]

        elif numRows == 2:
            return [[1],[1,1]]

        st = [[1],[1,1]]

        for i in range(2,numRows):
            li = [1]
            j = 0
            while j < len(st[-1])-1:
                n = st[-1][j] + st[-1][j+1]
                li.append(n)
                j += 1
            li.append(1)
            st.append(li)

        return st
