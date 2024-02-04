# PROBLEM:

# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# Example:

# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted

# SOLUTION:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if len(nums) > 0:
            mid = len(nums)//2
            node = TreeNode(val = nums[mid])
            node.left = self.sortedArrayToBST(nums[0 : mid])
            node.right = self.sortedArrayToBST(nums[mid + 1 : len(nums)])

            return node
