# PROBLEM:

# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]

# SOLUTION:

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]

        elif rowIndex == 1:
            return [1,1]

        st = [[1],[1,1]]

        for i in range(1,rowIndex):
            li = [1]
            j = 0
            while j < len(st[-1])-1:
                n = st[-1][j] + st[-1][j+1]
                li.append(n)
                j += 1
            li.append(1)
            st.append(li)

        return st[-1]

        
