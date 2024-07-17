# PROBLEM:

# Given the root of a binary tree, each node in the tree has a distinct value.

# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

# Return the roots of the trees in the remaining forest. You may return the result in any order.

# Example:

# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]

# SOLUTION:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res_set = set([root])

        def dfs(node):
            res = node
            if node != None:
                if node.val in to_delete:
                    res = None
                    res_set.discard(node)
                    if node.left: 
                        res_set.add(node.left)
                    if node.right:
                        res_set.add(node.right)
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                return res
        dfs(root)
        return list(res_set)
