# PROBLEM:

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example:

# Input: root = [1,2,2,3,4,4,3]
# Output: true

# SOLUTION:

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        li = []

        def traverse(root):

            if root != None:

                if root.left != None:
                    li.append(root.left.val)
                elif root.left == None:
                    li.append("*")
                
                traverse(root.left)
                traverse(root.right)

                if root.right != None:
                    li.append(root.right.val)
                elif root.right == None:
                    li.append("*")

        traverse(root)

        l = 0
        r = len(li)-1

        while l < r:
            
            if li[l] != li[r]:
                return False
            else:
                l += 1
                r -= 1

        return True
