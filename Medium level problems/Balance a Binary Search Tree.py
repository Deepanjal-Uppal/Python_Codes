# PROBLEM:

# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

# Example:

# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

# SOLUTION:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        li = []
        def traverse(root, li):
            if root != None:
                traverse(root.left, li)
                li.append(root.val)
                traverse(root.right, li)
                return li

        traverse(root, li)
        
        def binaryTree(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(li[mid])
            node.left = binaryTree(left, mid - 1)
            node.right = binaryTree(mid + 1, right)
            return node

        res = binaryTree(0, len(li) - 1)
        return res
             
