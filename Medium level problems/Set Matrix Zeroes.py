# PROBLEM:

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

# Example:

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# SOLUTION:

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])
        li = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    li.append([i,j])
        
        for i,j in li:
            for x in range(m):
                matrix[x][j] =0
            for y in range(n):
                matrix[i][y] = 0

        return matrix
