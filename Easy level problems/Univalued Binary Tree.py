# PROBLEM:

# A binary tree is uni-valued if every node in the tree has the same value.

# Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

# Example:

# Input: root = [1,1,1,1,1,null,1]
# Output: true

# SOLUTION:

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        uni = root.val
        flag = True

        def traverse(root):
            nonlocal flag
            if root != None:
                if root.val != uni:
                    flag = False
                traverse(root.left)
                traverse(root.right)
            return flag

        traverse(root)
        return flag
