# SOLUTION:

# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

# A leaf node is a node with no children.

# Example:

# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.

# SOLUTION:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node, curr_sum):
            nonlocal res
            if node != None:
                curr_sum += node.val
                if (node.left != None and node.right != None) or (node.left == None and node.right != None) or (node.left != None and node.right == None):
                    curr_sum *= 10
                    traverse(node.left, curr_sum)
                    traverse(node.right, curr_sum)
                elif node.left == None and node.right == None:
                    res += curr_sum

        p, res = 0, 0
        traverse(root, p)
        return res
