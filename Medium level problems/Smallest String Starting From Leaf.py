# PROBLEM:

# You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

# Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

# As a reminder, any shorter prefix of a string is lexicographically smaller.

# For example, "ab" is lexicographically smaller than "aba".
# A leaf of a node is a node that has no children.

# Example:

# Input: root = [0,1,2,3,4,3,4]
# Output: "dba"

# SOLUTION:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        def traverse(root, curr):
            if not root:
                return 
            curr = chr(ord('a') + root.val) + curr
            if root.left and root.right:
                return min(traverse(root.left, curr), traverse(root.right, curr))
            if root.right:
                return traverse(root.right, curr)
            if root.left:
                return traverse(root.left, curr)
            return curr
        return traverse(root, "")
