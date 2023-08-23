# PROBLEM:

# Given the root of a binary tree, invert the tree, and return its root.

# Example:

# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# SOLUTION:

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def traverse(curr):
            if curr != None:
                curr.left, curr.right = curr.right, curr.left
                traverse(curr.left)
                traverse(curr.right)
                
        curr = root
        traverse(curr)
        return root
