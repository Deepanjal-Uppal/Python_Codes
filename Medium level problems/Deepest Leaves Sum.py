# PROBLEM:

# Given the root of a binary tree, return the sum of values of its deepest leaves.
 
# Example:

# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15

# SOLUTION:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def heights(root):
            if root is None:
                return 0
            return 1 + max(heights(root.left), heights(root.right))

        depth = heights(root)

        def dfs(root, height):
            nonlocal res, depth
            if root != None:
                if height == depth:
                    res += root.val
                    return
                else:
                    dfs(root.left, height + 1)
                    dfs(root.right, height + 1)
        res = 0
        ans = dfs(root, 1)
        return res
