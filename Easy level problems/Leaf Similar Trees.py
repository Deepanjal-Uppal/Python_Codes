# PROBLEM:

# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

# Example:

# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true

# SOLUTION:
 
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1 = []
        l2 = []
        def traverse(root,l1):
            if root is not None:
                if root.left == None and root.right == None:
                    l1.append(root.val)
                traverse(root.left,l1)
                traverse(root.right,l1)
        traverse(root1,l1)
        traverse(root2,l2)

        if len(l1) == len(l2):
            for i in range(len(l1)):
                if l1[i] != l2[i]:
                    return False
            return True
        else:
            return False
