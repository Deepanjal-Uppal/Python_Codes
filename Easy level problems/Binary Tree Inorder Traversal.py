# PROBLEM:

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example:

# Input: root = [1,null,2,3]
# Output: [1,3,2]

# SOLUTION:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        li = []
        def traverse(root):
            if root != None:
                traverse(root.left)
                li.append(root.val)
                traverse(root.right)

        traverse(root)
        return li
