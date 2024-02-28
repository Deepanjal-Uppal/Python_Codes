# PROBLEM:

# Given the root of a binary tree, return the leftmost value in the last row of the tree.

# Example:

# Input: root = [2,1,3]
# Output: 1

# SOLUTION:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        if root.left == None and root.right == None:
            return root.val
        
        q = [root]
        while q:
            qlen = len(q)
            for i in range(qlen):
                node = q.pop(0)
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if len(q) > 0:
                lefty = q[0].val
            
        return lefty
