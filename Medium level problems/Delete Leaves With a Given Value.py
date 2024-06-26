# PROBLEM:

# Given a binary tree root and an integer target, delete all the leaf nodes with value target.

# Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, 
# it should also be deleted (you need to continue doing that until you cannot).

# Example:

# Input: root = [1,2,3,2,null,2,4], target = 2
# Output: [1,null,3,null,4]
# Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
# After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).

# SOLUTION:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def traverse(node):
            if node != None:
                traverse(node.left)
                traverse(node.right)
                if node != None and node.left != None:
                    if node.left.val == target and node.left.left == None and node.left.right == None:
                        node.left = None
                if node != None and node.right != None:
                    if node.right.val == target and node.right.left == None and node.right.right == None:
                        node.right = None
                
                

        traverse(root)
        if root.val == target and root.left == None and root.right == None:
                    return None
        return root
