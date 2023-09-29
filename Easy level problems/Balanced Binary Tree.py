# PROBLEM:

# Given a binary tree, determine if it is height-balanced.

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: true

# SOLUTION:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root == None:
            return True

        def height(root):
            if root == None:
                return 0
            left = height(root.left) 
            right = height(root.right)
            return 1 + max(left, right)
        
        left = height(root.left)
        right = height(root.right)

        if abs(left - right) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    
