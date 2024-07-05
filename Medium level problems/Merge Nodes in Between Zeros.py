# PROBLEM:

# You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

# For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. 
# The modified list should not contain any 0's.

# Return the head of the modified linked list.

# Example:

# Input: head = [0,3,1,0,4,5,2,0]
# Output: [4,11]
# Explanation: 
# The above figure represents the given linked list. The modified list contains
# - The sum of the nodes marked in green: 3 + 1 = 4.
# - The sum of the nodes marked in red: 4 + 5 + 2 = 11.

# SOLUTION:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        prev = res
        curr = head.next
        s = 0

        while curr != None:
            if curr.val == 0:
                new = ListNode(s)
                prev.next = new
                prev = prev.next
                s = 0
            else:
                s += curr.val
            curr = curr.next

        return res.next
