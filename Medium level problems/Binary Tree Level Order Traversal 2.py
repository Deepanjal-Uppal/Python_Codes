# PROBLEM:

# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

# Example:

# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]

# SOLUTION:

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        li = []
        li.append(root)

        while li:
            lilen = len(li)
            level = []
            for i in range(lilen):
                node = li.pop(0)
                if node:
                    level.append(node.val)
                    li.append(node.left)
                    li.append(node.right)
            if level:
                res.append(level)

        return res[::-1]
