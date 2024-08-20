# PROBLEM:

# Given the root of a binary tree and an integer targetSum,
# return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

# Example:

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.

# SOLUTION:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, s):
            nonlocal flag
            if node != None:
                if node.left == None and node.right == None and s == targetSum:
                    flag = True
                    return
                if node.left != None:
                    dfs(node.left, s + node.left.val)
                if node.right != None:
                    dfs(node.right, s + node.right.val)
            
        if root == None:
            return False
        flag = False
        dfs(root, root.val)
        return flag
        
