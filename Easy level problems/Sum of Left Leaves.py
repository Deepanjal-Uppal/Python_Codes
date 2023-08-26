# PROBLEM:

# Given the root of a binary tree, return the sum of all left leaves.

# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

# Example:

# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

# SOLUTION:

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def traverse(node):
            nonlocal s
            if node != None:
                if node.left != None:
                    if node.left.left == None and node.left.right == None:
                        s += node.left.val
                traverse(node.left)
                traverse(node.right)
        s = 0
        traverse(root)
        return s
