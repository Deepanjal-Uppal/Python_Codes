# PROBLEM:

# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

# Example:

# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

# SOLUTION:

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mini = []
        maxi = []

        for i in matrix:
            mini.append(min(i))

        for j in range(len(matrix[0])):
            ele = 0
            for i in range(len(matrix)):
                ele = max(ele, matrix[i][j])
            maxi.append(ele)

        res = []
        for i in mini:
            if i in maxi:
                res.append(i)
                
        return res
