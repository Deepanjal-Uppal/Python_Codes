# PROBLEM:

# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

# Example:

# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]

# SOLUTION:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        li = []
        res = []
        li.append(root)

        while li:
            lilen = len(li)
            level = []
            for i in range(lilen):
                node = li.pop(0)
                if node:
                    level.append(node.val)
                    li.append(node.left)
                    li.append(node.right)
            if len(level) > 0:
                m = max(level)
                res.append(m)

        return res
        
