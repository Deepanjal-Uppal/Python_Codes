# PROBLEM:

# Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. 
# If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. 
# More formally, the property root.val = min(root.left.val, root.right.val) always holds.

# Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

# If no such second minimum value exists, output -1 instead.

# Example:

# Input: root = [2,2,5,null,null,5,7]
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.

# SOLUTION:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        li = []
        def traverse(root):
            if root != None:
                traverse(root.left)
                li.append(root.val)
                traverse(root.right)
        
        traverse(root)
        m1 = min(li)
        m2 = max(li)

        for i in range(1,len(li)):
            if li[i] > m1 and li[i] < m2:
                m2 = li[i]
        if m1 == m2:
            return -1
        return m2
