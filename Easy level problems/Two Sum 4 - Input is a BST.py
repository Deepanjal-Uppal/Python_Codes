# PROBLEM:

# Given the root of a binary search tree and an integer k, 
# return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

# Example:

# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true

# SOLUTION:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        d = {}
        flag = False

        def traverse(root):
            nonlocal d, flag
            if root != None:
                diff = k - root.val
                if diff in d:
                    flag = True
                d[root.val] = 1
                traverse(root.left)
                traverse(root.right)
        
        

        traverse(root)
        return flag

 
