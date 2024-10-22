# PROBLEM:

# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

# Example:

# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.

# SOLUTION:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res, maxi = 0, float('-inf')
        li = [root]
        level = 1
        
        while li:
            lilen = len(li)
            curr = 0
            for i in range(lilen):
                node = li.pop(0)
                curr += node.val
                if node.left != None:
                    li.append(node.left)
                if node.right != None:
                    li.append(node.right)
            
            if curr > maxi:
                maxi = curr
                res = level
            level += 1
        
        return res
